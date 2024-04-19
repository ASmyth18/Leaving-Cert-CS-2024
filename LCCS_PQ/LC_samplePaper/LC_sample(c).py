# Question 16(c)
# Examination Number: 129478


def count_obese(bmi_values):
    return sum(bmi >= 30 for bmi in bmi_values)

def find_largest_and_second_largest(nums):
    largest = second_largest = float('-inf')
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return largest, second_largest if second_largest != float('-inf') else largest

def find_nth_largest(n, list_of_values):
    if n <= 0:
        return None
    return sorted(set(list_of_values), reverse=True)[n - 1] if n <= len(set(list_of_values)) else None

bmi_values = [24, 19, 33, 35, 27, 18, 15, 33, 35, 23, 32, 23]

obese_count = count_obese(bmi_values)
print(f"Obese: {obese_count}")

largest, second_largest = find_largest_and_second_largest(bmi_values)
print("Largest:", largest)
print("Second Largest:", second_largest)

print(find_nth_largest(3, bmi_values))