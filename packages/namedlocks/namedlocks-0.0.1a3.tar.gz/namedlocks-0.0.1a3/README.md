# NamedLocks

***
NamedLocks is a simple library for locking on a name.

## Installation

```pip install namedlocks```

## Usage

```python
import asyncio
from random import randint, uniform

from named_locks import AsyncNamedLock

NAMED_LOCKS = AsyncNamedLock()  # Create a global instance of the lock


async def task(uid: int):
    async with NAMED_LOCKS.lock(uid):  # Lock on some name
        print(f"Task {uid} started")
        # do something
        await asyncio.sleep(uniform(1, 5))
        print(f"Task {uid} finished")


async def main():
    tasks = [asyncio.create_task(task(uid)) for uid in [randint(1, 10) for _ in range(50)]]
    await asyncio.gather(*tasks)


asyncio.run(main())
```
