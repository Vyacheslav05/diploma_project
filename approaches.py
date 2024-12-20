# Asyncio

import asyncio
import aiohttp

async def asyncio_io_bound_task(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def asyncio_cpu_bound_task(n):
    return math.factorial(n)

async def asyncio_blocking_task(filename):
    with open(filename, "r") as f:
        await asyncio.sleep(2)  # Имитация чтения

# Threading
import threading

def threading_io_bound_task(url):
    response = requests.get(url)
    return response.text

def threading_cpu_bound_task(n):
    return math.factorial(n)

def threading_blocking_task(filename):
    with open(filename, "r") as f:
        time.sleep(2)  # Имитация чтения

# Multiprocessing
from multiprocessing import Pool

def multiprocessing_io_bound_task(url):
    response = requests.get(url)
    return response.text

def multiprocessing_cpu_bound_task(n):
    return math.factorial(n)

def multiprocessing_blocking_task(filename):
    with open(filename, "r") as f:
        time.sleep(2)  # Имитация чтения