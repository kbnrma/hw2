

def decorator_function(func):
    def wrapper():
        print("Начало декоратора")
        func()
        print("Конец декоратора")
    return wrapper

@decorator_function
def hello_geeks():
    print("Hello From Geeks Backend Group 09!")
hello_geeks()   

import time, requests

def benchmark(func):
    def wrapper(url):
        start = time.time()
        func(url)
        end = time.time()
        print(f"Время выполнения запроса {end-start} сек")
    return wrapper

@benchmark
def send_rrequest(url):
    webpage = requests.get(url)
send_rrequest('https://google.com')

@benchmark
def time_work_code(obj):
    print("Hello World")
    geeks = "gEEkS"
    print(geeks.title())
    for i in range(100):
        print(i)
time_work_code('Janysh')