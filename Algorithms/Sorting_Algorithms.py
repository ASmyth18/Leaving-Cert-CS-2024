import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def shufflesort(arr):
    while True:
        shuffled = arr[:]
        random.shuffle(shuffled)
        if shuffled == sorted(arr):
            return shuffled

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)

print("Quicksort:")
sorted_arr = quicksort(arr)
print(sorted_arr)

print("Bubblesort:")
sorted_arr = bubblesort(arr)
print(sorted_arr)

print("Shufflesort:")
sorted_arr = shufflesort(arr)
print(sorted_arr)