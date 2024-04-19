# Question 16(a)
# Examination Number: 129478

def display_intro():
    print("Welcome to my BMI calculator!")

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obese"

def calculate_bmi(weight, height):
    return round(weight / (height ** 2) * 10000, 1)

def main():
    display_intro()
    weight = float(input("Enter weight (in kilograms): "))
    height = float(input("Enter height (in centimeters): "))

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"BMI is: {bmi}")
    print(f"BMI Category: {category}")

if __name__ == "__main__":
    main()

