import time
import requests
import math

# I/O-bound задача: загрузка данных с веб-сайта
def io_bound_task(url):
    response = requests.get(url)
    return response.text

# CPU-bound задача: вычисление факториала
def cpu_bound_task(n):
    return math.factorial(n)

# Блокирующая задача: чтение файла
def blocking_task(filename):
    with open(filename, "r") as f:
        time.sleep(2)  # Имитация чтения