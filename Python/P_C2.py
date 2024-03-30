import functools
import itertools
import threading
import time

# Decorators
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.5f} seconds")
        return result
    return wrapper

# Generators
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Lambda Functions
square = lambda x: x ** 2
print(square(5))

# Map, Filter, Reduce
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
product = functools.reduce(lambda x, y: x * y, numbers)
print(squared_numbers)
print(even_numbers)
print(product)

# Itertools
combinations = list(itertools.combinations(numbers, 3))
permutations = list(itertools.permutations(numbers, 2))
print(combinations)
print(permutations)

# Multithreading
def worker(thread_id):
    print(f"Thread {thread_id} started.")
    time.sleep(2)
    print(f"Thread {thread_id} finished.")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Decorators Usage
@timer
def calculate_sum(n):
    return sum(range(n))

result = calculate_sum(10000000)
print(f"Sum: {result}")

# Generators Usage
fib = fibonacci()
for _ in range(10):
    print(next(fib))