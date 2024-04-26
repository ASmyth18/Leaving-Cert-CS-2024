# This function counts the number of BMI values that are greater than or equal to 30,
# which indicates obesity.
def count_obese(bmi_values):
    return sum(bmi >= 30 for bmi in bmi_values)

# This function finds the largest and second largest numbers in a list.
def find_largest_and_second_largest(nums):
    largest = second_largest = float('-inf')  # Initializing variables to negative infinity.
    for num in nums:  # Looping through each number in the input list.
        if num > largest:  # Checking if the current number is greater than the largest.
            second_largest = largest  # Updating the second largest to the previous largest.
            largest = num  # Updating the largest to the current number.
        elif num > second_largest and num != largest:  # Checking if the number is greater than the second largest.
            second_largest = num  # Updating the second largest if conditions are met.
    return largest, second_largest if second_largest != float('-inf') else largest  # Returning the largest and second largest numbers.

# This function finds the nth largest number in a list.
def find_nth_largest(n, list_of_values):
    if n <= 0:  # Checking if n is less than or equal to 0.
        return None
    # Using set() to remove duplicates, sorting the list in descending order,
    # and then selecting the nth element if it exists.
    return sorted(set(list_of_values), reverse=True)[n - 1] if n <= len(set(list_of_values)) else None

# List of BMI values.
bmi_values = [24, 19, 33, 35, 27, 18, 15, 33, 35, 23, 32, 23]

# Counting the number of obese BMI values.
obese_count = count_obese(bmi_values)
print(f"Obese: {obese_count}")  # Printing the count of obese BMI values.

# Finding the largest and second largest BMI values.
largest, second_largest = find_largest_and_second_largest(bmi_values)
print("Largest:", largest)  # Printing the largest BMI value.
print("Second Largest:", second_largest)  # Printing the second largest BMI value.

# Finding the 3rd largest BMI value.
print(find_nth_largest(3, bmi_values))  # Printing the 3rd largest BMI value.
