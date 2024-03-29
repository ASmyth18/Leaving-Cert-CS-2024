import sys

# O(1) - Constant Space
def constant_space(n):
    x = 1
    y = 2
    return x + y

# O(n) - Linear Space
def linear_space(n):
    arr = [0] * n
    return sum(arr)

# O(n^2) - Quadratic Space
def quadratic_space(n):
    matrix = [[0] * n for _ in range(n)]
    return sum(sum(row) for row in matrix)

# O(log n) - Logarithmic Space
def logarithmic_space(n):
    if n <= 1:
        return 1
    return logarithmic_space(n // 2) + 1

# O(2^n) - Exponential Space
def exponential_space(n):
    if n == 0:
        return 1
    return exponential_space(n - 1) + exponential_space(n - 1)

# Measure space usage for different space complexities
def measure_space(func, n):
    space_usage = sys.getsizeof(func(n))
    print(f"Space usage for {func.__name__}: {space_usage} bytes")

# Test the space complexities
n = 10

print("Space Complexity Analysis:")
measure_space(constant_space, n)
measure_space(linear_space, n)
measure_space(quadratic_space, n)
measure_space(logarithmic_space, n)
measure_space(exponential_space, n)