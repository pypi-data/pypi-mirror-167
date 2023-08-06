#!/usr/bin/env python

"""
Master-Worker模型-协程实现方式
"""

from __future__ import annotations

import asyncio
from asyncio.futures import Future
from typing import Callable, Coroutine, List

__all__ = ["Master", "Worker"]


class Worker(object):
    def __init__(self, func: Callable[..., Coroutine], *args, **kargs):
        self._func = func
        self._args = args
        self._kargs = kargs

    async def __call__(self):
        return await self._func(*self._args, **self._kargs)


class Master(object):
    def __init__(self):
        self._workers: List[Worker] = []
        self._done_callbacks: List[Callable[[Future]]] = []

    def add_worker(self, worker: Worker):
        self._workers.append(worker)

    def add_done_callback(self, callback: Callable[[Future]]):
        self._done_callbacks.append(callback)

    async def start(self):
        tasks = []
        for worker in self._workers:
            task = asyncio.ensure_future(worker())
            for callback in self._done_callbacks:
                task.add_done_callback(callback)
            tasks.append(task)
        return await asyncio.gather(*tasks)
