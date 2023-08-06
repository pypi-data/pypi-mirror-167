# -*- coding: utf-8 -*-
import abc
import os
import pickle
import shutil
from typing import List, Optional

import hao
import lmdb
import rocksdbpy
from hao.namespaces import attr, from_args
from hao.singleton import Singleton
from tailors.domains import Derivable
from tailors.models import TailorsIO
from torch.utils.data import Dataset
from torch.utils.data.dataloader import DataLoader
from torch.utils.data.distributed import DistributedSampler
from tqdm import tqdm

from tailors_trainer.exceptions import TailorsTrainerError

LOGGER = hao.logs.get_logger(__name__)


class CacheStore(abc.ABC, Derivable):

    @staticmethod
    def get_instance(name, cache_dir, split) -> 'CacheStore':
        for clz in CacheStore.subclasses():
            if clz.name() == name:
                return clz(cache_dir, split)
        raise TailorsTrainerError(f"Unsupported cache type: {name}")

    def __init__(self, cache_dir: str, split: str) -> None:
        self.path = hao.paths.get(f"data/cache/{cache_dir}/{split}.{self.name()}")
        hao.paths.make_parent_dirs(self.path)
        self.db: Optional[lmdb.Environment] = None
        self.length = -1
        self.keys = None

    @staticmethod
    @abc.abstractmethod
    def name():
        raise NotImplementedError()

    @staticmethod
    def serialize(data) -> bytes:
        return pickle.dumps(data)

    @staticmethod
    def unserialize(data: bytes):
        return pickle.loads(data)

    @abc.abstractmethod
    def load(self) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def populate(self, items):
        raise NotImplementedError()

    @abc.abstractmethod
    def get(self, index):
        raise NotImplementedError()

    @abc.abstractmethod
    def size(self) -> int:
        raise NotImplementedError()


class NoneCacheStore(CacheStore):
    def __init__(self, dir: str, split: str) -> None:
        super().__init__(dir, split)
        self.path = None
        self.items = None

    @staticmethod
    def name():
        return 'none'

    def load(self) -> bool:
        return self.items is not None and len(self.items) > 0

    def populate(self, items):
        self.items = list(items)

    def get(self, index):
        return self.items[index]

    def size(self):
        return len(self.items)


class LmdbCacheStore(CacheStore):

    @staticmethod
    def name():
        return 'lmdb'

    def load(self) -> bool:
        if not os.path.exists(self.path):
            return False

        try:
            self.db = self.open_db()
            with self.db.begin(write=False) as txn:
                self.length = txn.stat()["entries"]
                self.keys = [key for key, _ in txn.cursor()]
                return self.length > 0
        except Exception:
            hao.paths.delete(f"{self.path}*")
            return False

    def populate(self, items):
        with self.open_db(readonly=False) as db:
            txn = db.begin(write=True)
            for i, item in enumerate(items):
                txn.put(f"{i}".encode("ascii"), self.serialize(item))
                if i % 201 == 0:
                    txn.commit()
                    txn = db.begin(write=True)
            txn.commit()

    def get(self, index: int):
        with self.db.begin(write=False) as txn:
            return self.unserialize(txn.get(self.keys[index]))

    def open_db(self, readonly: bool = True) -> lmdb.Environment:
        return lmdb.open(
            self.path,
            subdir=False,
            readonly=readonly,
            lock=not readonly,
            readahead=False,
            meminit=False,
            map_size=1099511627776 * 2,
            map_async=True
        )

    def size(self):
        return self.length


class RocksdbCacheStore(CacheStore):

    @staticmethod
    def name():
        return 'rocksdb'

    def load(self) -> bool:
        if not os.path.exists(self.path):
            return False

        try:
            self.db = self.open_db()
            self.length = self.get('total')
            return self.length > 0
        except Exception:
            hao.paths.delete(f"{self.path}*")
            return False

    def populate(self, items):
        db = self.open_db(readonly=False)
        try:
            total = 0
            for i, item in enumerate(items):
                db.set(f"{i}".encode('ascii'), self.serialize(item))
                total += 1
            db.set('total'.encode('ascii'), self.serialize(total))
            db.flush()
        finally:
            db.close()

    def get(self, key):
        return self.unserialize(self.db.get(f"{key}".encode('ascii')))

    def size(self):
        return self.length

    def open_db(self, readonly: bool = True):
        option = rocksdbpy.Option()
        option.create_if_missing(True)
        option.set_max_open_files(100)
        option.set_use_fsync(False)
        option.set_bytes_per_sync(1024 * 1024)
        option.optimize_for_point_lookup(1024 * 1024)
        if readonly:
            return rocksdbpy.open_for_readonly(self.path, option)
        else:
            return rocksdbpy.open(self.path, option)


def cache_names() -> tuple:
    return tuple(clz.name() for clz in CacheStore.subclasses())


@from_args
class DatasetConf(metaclass=Singleton):
    shuffle: bool = attr(bool, default=True)
    drop_last: bool = attr(bool, default=True)
    bz = attr(int, default=128)
    pin_mem: bool = attr(bool, default=True)
    workers = attr(int, default=0)
    cache = attr(str, choices=cache_names(), default=RocksdbCacheStore.name())


class TailorDataset(Dataset):
    def __init__(self, io: TailorsIO, name: str, split: str, files: List[str], dataset_conf: DatasetConf) -> None:
        super().__init__()
        self.io = io
        self.name = name
        self.split = split
        self.files = files if isinstance(files, list) else [files]
        self.ddp = False  # todo
        self.dataset_conf = dataset_conf
        self.cache = CacheStore.get_instance(dataset_conf.cache, f"{self.io.__module__}/{self.name}", self.split)

    def load(self):
        if not self.cache.load():
            try:
                self.cache.populate(self.from_files())
            except KeyboardInterrupt:
                shutil.rmtree(self.cache.path)
            if not self.cache.load():
                raise TailorsTrainerError(f'Failed to load/populate cache: {self.dataset_conf.cache}')
        LOGGER.info(f"[dataset] split: {self.split}, size: {self.cache.size()}, cache: {self.cache.path or 'n/a'}")
        return self

    def from_files(self):
        for file in self.files:
            yield from self.from_file(file)

    def from_file(self, file):
        filepath = hao.paths.get(file)
        if not os.path.exists(filepath):
            raise TailorsTrainerError(f"[dataset] file not found, corpus: {self.name}, split: {self.split}, file: {file}")

        tqdm_opts = {'desc': f"[dataset] {os.path.basename(filepath): <20}", 'ascii': '░▒▓', 'colour': 'cyan'}
        if (from_lines := getattr(self.io, 'from_lines', None)) is not None:
            for data in tqdm(from_lines(open(filepath, 'r').read()), **tqdm_opts):
                yield data

        else:
            n_lines = hao.files.count_lines(filepath)
            with open(filepath, "r") as f:
                for line in tqdm(f, total=n_lines, **tqdm_opts):
                    line = hao.strings.strip_to_none(line)
                    if line is None:
                        continue
                    yield from self.from_line(line)

    def from_line(self, line: str):
        return self.io.from_line(line)

    def __getitem__(self, index: int):
        return self.cache.get(index)

    def __len__(self) -> int:
        return self.cache.size()

    def dataloader(self):
        self.load()
        if self.ddp:
            return DataLoader(
                self,
                batch_size=self.dataset_conf.bz,
                num_workers=self.dataset_conf.workers,
                pin_memory=self.dataset_conf.pin_mem,
                drop_last=self.dataset_conf.drop_last,
                collate_fn=self.io.collate,
                sampler=DistributedSampler(self)
            )
        return DataLoader(
            self,
            batch_size=self.dataset_conf.bz,
            num_workers=self.dataset_conf.workers,
            pin_memory=self.dataset_conf.pin_mem,
            drop_last=self.dataset_conf.drop_last,
            shuffle=self.dataset_conf.shuffle,
            collate_fn=self.io.collate,
        )
