# -*- coding: utf-8 -*-
import sys
import warnings

import hao
import regex
from hao.namespaces import attr, from_args

from tailors_trainer.exceptions import TailorsTrainerError
from tailors_trainer.trainer import Trainer

warnings.filterwarnings("ignore")
LOGGER = hao.logs.get_logger(__name__)


@from_args
class TaskConf:
    task: str = attr(str, help='using predefined values in `tasks.{task}` in tailors.yml')


def parse_args() -> dict:
    args_str = ' '.join(sys.argv[1:])
    args = [regex.compile(r'(?:\s*=\s*|\s+)').split(item) for item in regex.compile(r'\s*\-{2}').split(args_str) if item]
    return {a[0]: a[1] if len(a) == 2 else None for a in args}


def log_cmdline():
    arguments = [f"--{k}={v}" if v else f"--{k}" for k, v in parse_args().items()]
    n_args = len(arguments)

    sep = ' ' if n_args <= 1 else ' \\\n\t'
    args = sep.join(arguments)
    LOGGER.info(f"\n{'━' * 50}\ntailors-train{sep}{args}\n{'━' * 50}")


def load_task():
    task_conf = TaskConf()
    if task_conf.task is None:
        return
    task = hao.config.get(f"tasks.{task_conf.task}", config='tailors.yml')
    if task is None or len(task) == 0:
        return
    args = parse_args()
    arguments = [f"--{k}={v}" for k, v in task.items() if k not in args]
    sys.argv.extend(arguments)


def train():
    try:
        log_cmdline()
        load_task()
        trainer = Trainer()
        trainer.fit()
    except KeyboardInterrupt:
        print("[ctrl-c] stopped")
    except TailorsTrainerError as err:
        LOGGER.error(err)
    except Exception as err:
        LOGGER.exception(err)


if __name__ == "__main__":
    train()
