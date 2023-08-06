#!/usr/bin/env python

"""
Master-Worker模型-多线程实现方式
"""

from __future__ import annotations

from concurrent.futures import Future, ThreadPoolExecutor
from typing import Callable, List

__all__ = ["Master", "Worker"]


class Worker(object):
    def __init__(self, func, *args, **kargs):
        self._func = func
        self._args = args
        self._kargs = kargs

    def __call__(self):
        return self._func(*self._args, **self._kargs)


class Master(object):
    def __init__(self, max_workers: int = None):
        self._executor = ThreadPoolExecutor(max_workers=max_workers)
        self._workers: List[Worker] = []
        self._done_callbacks: List[Callable[[Future]]] = []

    def add_worker(self, worker: Worker):
        self._workers.append(worker)

    def add_done_callback(self, callback: Callable[[Future]]):
        self._done_callbacks.append(callback)

    def start(self):
        for worker in self._workers:
            t = self._executor.submit(worker)
            for callback in self._done_callbacks:
                t.add_done_callback(callback)

    def wait(self):
        self._executor.shutdown()
