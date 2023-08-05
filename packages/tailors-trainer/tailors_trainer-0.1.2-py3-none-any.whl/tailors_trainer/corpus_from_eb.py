# -*- coding: utf-8 -*-
import itertools
import json
import logging
import operator
import os
import random
from collections import Counter
from typing import List, Optional, Tuple

import hao
from hao.mongo import Mongo
from hao.namespaces import attr, from_args
from hao.stopwatch import Stopwatch
from tqdm import tqdm

LOGGER = hao.logs.get_logger(__name__)
hao.logs.update_logger_levels({
    "__main__": logging.INFO,
})


@from_args
class Conf(object):
    task: str = attr(str, default='bidding')
    reviewed_only: bool = attr(bool, action='store_true')
    cases: bool = attr(bool, default=True)
    cases_factor: int = attr(int, default=2, help='n duplicates of the cases')
    cases_starts: int = attr(int, help='No. from which are all cases')
    size: int = attr(int)
    seed: int = attr(int, required=True, default=1000)
    query: str = attr(str)


def process():
    LOGGER.info('process')
    sw = Stopwatch()
    conf = Conf()
    LOGGER.info(conf)

    task_name = conf.task if conf.task.startswith("task-") else f"task-{conf.task}"
    task_cases_name = f"{task_name}-cases"

    mongo = Mongo()
    task_exist, task_cases_exist = mongo.is_collection_exist(task_name), mongo.is_collection_exist(task_cases_name)
    if not task_exist and not task_cases_exist:
        LOGGER.info('tasks not exist')
        return

    items = list(from_eb(mongo, task_name, conf.reviewed_only, conf.size, conf.query))
    items_cases = []

    items_train = [item for item in items if item.get('splits', {}).get(conf.seed) == 'train']
    items_val = [item for item in items if item.get('splits', {}).get(conf.seed) == 'val']

    if len(items_train) > 0 and len(items_val) > 0:
        items_cases = [item for item in items if item.get('split', {}).get(conf.seed) not in ('train', 'val')]

    else:
        LOGGER.info('no pre splits on seed')
        if conf.cases and task_cases_exist:
            items_cases = list(from_eb(mongo, task_cases_name, conf.reviewed_only, conf.size, conf.query))
        elif conf.cases_starts and conf.cases_starts < len(items):
            items_cases = items[conf.cases_starts:]
            items = items[:conf.cases_starts]
        random.seed(conf.seed)
        random.shuffle(items)
        i = int(0.8 * len(items))
        items_train = items[:i]
        items_val = items[i:]

    corpus = {
        'train': items_train + items_cases * conf.cases_factor,
        'val': items_val
    }
    msgs = []
    for split, items in corpus.items():
        msg = save_to_file(conf.task, split, items)
        log_summary(split, items)
        msgs.append(msg)

    LOGGER.info(f'done, took: {sw.took()}')
    for msg in msgs:
        LOGGER.info(msg)


def from_eb(mongo: Mongo, col_name: str, reviewed_only: bool = False, size: Optional[int] = None, query: Optional[str] = None):
    LOGGER.info(f"[from eb] task: {col_name}, reviewed_only: {reviewed_only}, size: {size}, query: {query}")
    _query = {'enabled': {'$ne': False}, 'editor_timestamp': {'$ne': None}, 'annotation': {'$exists': True}}
    if query is not None:
        query = {**_query, **json.loads(query)}
    else:
        query = _query
        if reviewed_only:
            query['reviewer_timestamp'] = {'$ne': None}

    total = mongo.count(col_name, query)
    if size is not None:
        total = min(size, total)

    projection = {'uid': 1, 'es_id': 1, 'caption': 1, 'html': 1, 'text': 1, 'annotation': 1}
    for item in tqdm(mongo.find(col_name, query, projection).limit(total), total=total, desc=f"[fetching] {col_name}"):
        data = convert_annotations(item)
        if data:
            yield data


def convert_annotations(item):
    annotation = item.get('annotation')
    if annotation is None or len(annotation) == 0:
        return

    entities, relations = get_entities_and_relations(annotation)
    label, labels = get_classifications(annotation)
    data = {
        'uid': item.get('uid'),
        'es_id': item.get('es_id'),
        'caption': item.get('caption'),
        'text': item.get('text'),
        'html': item.get('html'),
        'label': label,
        'labels': labels,
        'entities': entities,
        'relations': relations,
        'splits': item.get('splits')
    }
    return {k: v for k, v in data.items() if v is not None}


def get_entities_and_relations(annotation: dict) -> Tuple[list, list]:
    annotations_ner, annotations_re = annotation.get("NER"), annotation.get("RE")
    if annotations_ner is None:
        return None, None
    if len(annotations_ner) == 0:
        if annotations_re is None:
            return [], None
        else:
            return [], []

    idx = itertools.count(0)
    annotations_ner = [list(sorted(tags, key=operator.itemgetter('span_start'))) for tags in annotations_ner]
    entities = [[transform_tag(tag, next(idx)) for tag in tags] for tags in annotations_ner]
    entity_id_to_idx = [
        {str(tag.get('id')): {'j': j, 'idx': tag.get('idx')} for j, tag in enumerate(tags)}
        for tags in entities
    ]
    relations = [transform_rel(rel, entity_id_to_idx) for rel in annotations_re] if annotations_re else []
    return entities, relations


def transform_tag(tag, idx):
    return {
        'id': str(tag.get('id')),
        'tag': tag.get('name'),
        'start': tag.get('span_start'),
        'end': tag.get('span_end'),
        'idx': idx,
    }


def transform_rel(rel, entity_id_to_idx):
    s = rel.get('s')
    o = rel.get('o')
    p = rel.get('p')
    s = {'i': s.get('i'), **entity_id_to_idx[s.get('i')].get(str(s.get('id')))}
    o = {'i': o.get('i'), **entity_id_to_idx[o.get('i')].get(str(o.get('id')))}
    p = p.get('name')
    return {'s': s, 'o': o, 'p': p}


def get_classifications(annotation: dict):
    return annotation.get('SLC'), annotation.get('MLC')


def save_to_file(task: str, split: str, items: List[dict]):
    filepath = hao.paths.get(f"data/corpus/{task}/{split}.jsonl")
    hao.paths.make_parent_dirs(filepath)
    with open(filepath, "w") as f:
        for item in tqdm(items, desc=f"[saving] {os.path.basename(filepath)}"):
            f.write(f"{hao.jsons.dumps(item)}\n")
    return f"saved to {filepath}, size: {len(items)}"


def log_summary(split, items):
    counter_tags, counter_relations, counter_labels, counter_seed = Counter(), Counter(), Counter(), Counter()
    LOGGER.info(f" {split} ".center(60, '='))
    for item in items:
        entities, relations, label, labels = item.get('entities'), item.get('relations'), item.get('label'), item.get('labels')
        for entries in entities:
            counter_tags.update([entry.get('tag') for entry in entries])
        counter_relations.update([relation.get('p') for relation in relations])
        if label:
            counter_labels.update((label,))
        if labels:
            counter_labels.update(labels)
        counter_seed.update(list(item.get('splits', [])))

    if len(counter_tags) > 0:
        LOGGER.info(" entities ".center(35, '-'))
        size = max([len(tag) for tag in counter_tags]) + 1
        for seed, count in counter_tags.items():
            LOGGER.info(f"\t{seed: <{size}}: {count}")

    if len(counter_relations) > 0:
        LOGGER.info(" relations ".center(35, '-'))
        size = max([len(tag) for tag in counter_relations]) + 1
        for seed, count in counter_relations.items():
            LOGGER.info(f"\t{seed: <{size}}: {count}")

    if len(counter_labels) > 0:
        LOGGER.info(" labels ".center(35, '-'))
        size = max([len(tag) for tag in counter_labels]) + 1
        for seed, count in counter_labels.items():
            LOGGER.info(f"\t{seed: <{size}}: {count}")

    if len(counter_seed) > 0:
        LOGGER.info(" seeds ".center(35, '-'))
        size = max([len(str(seed)) for seed in counter_seed]) + 1
        for seed, count in counter_seed.items():
            LOGGER.info(f"\t{seed: <{size}}: {count}")



if __name__ == '__main__':
    try:
        process()
    except KeyboardInterrupt:
        print('[ctrl-c] stopped')
    except Exception as e:
        LOGGER.exception(e)
