import asyncio
import logging
from abc import ABC
from asyncio import Lock
from collections import defaultdict
from contextlib import asynccontextmanager
from typing import Hashable

from named_locks.base_named_lock import BaseNamedLock

logger = logging.getLogger(__name__)


class AsyncNamedLock(BaseNamedLock, ABC):
    def __init__(self):
        super().__init__()
        self._locks: defaultdict[Hashable, Lock] = defaultdict(asyncio.Lock)

    def _cleanup(self, name: Hashable):
        if self._locks[name]._waiters is None:  # noqa
            logger.debug("Cleanup %s, because waiters is None" % name)
            del self._locks[name]

        elif len(self._locks[name]._waiters) == 0:  # noqa
            logger.debug("Cleanup %s, because waiters is empty" % name)
            del self._locks[name]

    @asynccontextmanager
    async def lock(self, name: Hashable):
        logger.debug("Acquire lock for %s" % name)
        async with self._locks[name]:
            yield

        logger.debug("Release lock for %s" % name)
        self._cleanup(name)
