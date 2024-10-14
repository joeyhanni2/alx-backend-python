#!/usr/bin/env python3
"""This module contains an asynchronous coroutine
that waits for a random delay and returns it.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:

delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main() -> None:

"""Calls wait_random coroutine and prints the result."""
    random_delay: float = await wait_random(5)
    print(f"Waited for {random_delay:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
