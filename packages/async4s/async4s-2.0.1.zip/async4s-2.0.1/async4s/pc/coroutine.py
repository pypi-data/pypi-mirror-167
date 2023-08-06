#!/usr/bin/env python

"""
Producer-Comsumer模型-协程实现方式
"""

from __future__ import annotations

import asyncio
import abc


class PC(metaclass=abc.ABCMeta):
    def __init__(self, buffer_size=1024):
        self.buffer = asyncio.Queue(buffer_size)

    @abc.abstractmethod
    async def produce(self):
        pass

    @abc.abstractmethod
    async def comsume(self):
        pass

    async def start(self):
        producer = asyncio.ensure_future(self.produce())
        comsumer = asyncio.ensure_future(self.comsume())
        return await asyncio.gather(producer, comsumer)
