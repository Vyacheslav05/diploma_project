import asyncio
from tasks import io_bound_task, cpu_bound_task, blocking_task
from approaches import (
    asyncio_io_bound_task, asyncio_cpu_bound_task, asyncio_blocking_task,
    threading_io_bound_task, threading_cpu_bound_task, threading_blocking_task,
    multiprocessing_io_bound_task, multiprocessing_cpu_bound_task, multiprocessing_blocking_task,
)
from comparison import measure_performance

# CLI для выбора задачи и подхода
def main():
    print("Выберите задачу:")
    print("1. I/O-bound")
    print("2. CPU-bound")
    print("3. Блокирующая задача")
    task_choice = int(input("Введите номер задачи: "))

    print("Выберите подход:")
    print("1. Asyncio")
    print("2. Threading")
    print("3. Multiprocessing")
    approach_choice = int(input("Введите номер подхода: "))

# Определение выбранной задачи и подхода
    if task_choice == 1:  # I/O-bound
        task = io_bound_task
        async_task = asyncio_io_bound_task
        threading_task = threading_io_bound_task
        multiprocessing_task = multiprocessing_io_bound_task
        args = ["http://example.com"]
    elif task_choice == 2:  # CPU-bound
        task = cpu_bound_task
        async_task = asyncio_cpu_bound_task
        threading_task = threading_cpu_bound_task
        multiprocessing_task = multiprocessing_cpu_bound_task
        args = [10]
    elif task_choice == 3:  # Блокирующая задача
        task = blocking_task
        async_task = asyncio_blocking_task
        threading_task = threading_blocking_task
        multiprocessing_task = multiprocessing_blocking_task
        args = ["large_file.txt"]

# Выполнение задачи с выбранным подходом
    if approach_choice == 1:  # Asyncio
        result = asyncio.run(async_task(*args))
    elif approach_choice == 2:  # Threading
        result = threading_task(*args)
    elif approach_choice == 3:  # Multiprocessing
        with Pool(processes=4) as pool:
            result = pool.apply(multiprocessing_task, args)

# Измерение производительности
    performance = measure_performance(task, *args)
    print(f"Результат: {result}")
    print(f"Время выполнения: {performance['time']:.4f} сек")
    print(f"Потребление памяти: {performance['memory']} байт")

if __name__ == "__main__":
    main()