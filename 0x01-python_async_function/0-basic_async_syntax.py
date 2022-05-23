#!/usr/bin/env python3
"""asynchronous routine"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """await random delay btn 0 and max_delay"""
    random_number = random.random() * max_delay
    await asyncio.sleep(random_number)
    return random_number
