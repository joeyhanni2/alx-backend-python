#!/usr/bin/env python3
"""This module provides a function to create an asyncio.Task
for the wait_random coroutine.
"""

import asyncio
from 0_basic_async_syntax import wait_random



def task_wait_random(max_delay: int) -> asyncio.Task:


    return asyncio.create_task(wait_random(max_delay))
