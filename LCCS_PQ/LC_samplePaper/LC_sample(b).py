# Question 16(b)
# Examination Number: 129478

# For this question it is useful to understand ...
# 1. randint(a, b) returns a random integer N such that a<=N<=b.
# 2. s.append(x) appends the element x to the end of list s.

from random import randint # Import the randint function from the random module

def calculate_bmi(height, weight): # Define a function to calculate BMI
    return round(weight / ((height / 100) ** 2), 1) # Calculate BMI and round the result to 1 decimal place

amount = int(input("Enter the number of pairs of values you wish to generate: ")) # Get the number of pairs of values from user input

heights = [randint(150, 210) for _ in range(amount)] # Generate a list of random heights between 150 and 210
weights = [randint(50, 130) for _ in range(amount)] # Generate a list of random weights between 50 and 130
bmi_values = [calculate_bmi(h, w) for h, w in zip(heights, weights)] # Calculate BMI values for each pair of height and weight

print(f"Heights: {heights}\nWeights: {weights}\nBMI Values: {bmi_values}") # Print the lists of heights, weights, and BMI values
