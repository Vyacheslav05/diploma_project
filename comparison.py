import time
import psutil

def measure_performance(func, *args):
    start_time = time.perf_counter()
    process = psutil.Process()
    initial_memory = process.memory_info().rss

    result = func(*args)

    end_time = time.perf_counter()
    final_memory = process.memory_info().rss

    return {
        "time": end_time - start_time,
        "memory": final_memory - initial_memory,
        "result": result,
    }