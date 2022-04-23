#!/usr/bin/env python3
""" function that waits for a random number of seconds """

import asyncio
import random


async def wait_random(max_delay=10):
    """
    asynchronous coroutine that
    waits for a random delay between 0 and max_delay
    :param max_delay: maximum number of seconds to wait
    return: number of seconds waited
    """
    t = random.uniform(0, max_delay)
    await asyncio.sleep(t)
    return t
