# Question 16(a)
# Examination Number: 129478

print("*******************")
print("Times Table program") # Change from “Multiplication program”
print("*******************")

number = int(input("Please enter a number to be used as the multiplier: "))

# print("Multiplications of ", number)

if number < 0:
    print("Negative numbers are not accepted")
else:
    print("Multiplications of ", number)
    for i in range(13): # Changed range from 10 to 13
        print(f"{i} x {number} = {i * number}")
