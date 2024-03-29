import time

# O(1) - Constant Time
def constant_time(n):
    return n * 2

# O(log n) - Logarithmic Time
def logarithmic_time(n):
    i = 1
    while i < n:
        i *= 2

# O(n) - Linear Time
def linear_time(n):
    for i in range(n):
        pass

# O(n log n) - Linearithmic Time
def linearithmic_time(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 2

# O(n^2) - Quadratic Time
def quadratic_time(n):
    for i in range(n):
        for j in range(n):
            pass

# O(2^n) - Exponential Time
def exponential_time(n):
    if n <= 1:
        return
    exponential_time(n - 1)
    exponential_time(n - 1)

# O(n!) - Factorial Time
def factorial_time(n):
    if n == 0:
        return
    for i in range(n):
        factorial_time(n - 1)

# Measure execution time for different time complexities
def measure_time(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time for {func.__name__}: {execution_time:.6f} seconds")

# Test the time complexities
n = 10

print("Time Complexity Analysis:")
measure_time(constant_time, n)
measure_time(logarithmic_time, n)
measure_time(linear_time, n)
measure_time(linearithmic_time, n)
measure_time(quadratic_time, n)
measure_time(exponential_time, n)
# measure_time(factorial_time, n)  # Uncomment this line to test factorial time (Only do so if you have a modern computer)