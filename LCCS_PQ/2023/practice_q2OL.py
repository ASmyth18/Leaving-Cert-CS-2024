# Question 16(b)
# Examination Number: 129478

print("Welcome to the Temperature Alert System")

temp = int(input("Please enter a temperature value in degrees Celsius: "))

if temp < 20:
    print("Too cold. Turn up heating")
elif temp >= 20 and temp <= 24:
    print("Temperature is just right")
elif temp > 24:
    print("Too warm. Turn down heating")
    