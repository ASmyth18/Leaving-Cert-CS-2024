# Question 16 (a)
# Examination Number: 129478

firstName = input("What is your first name? ")
surname = input("What is your surname? ")

print(f"Hello {firstName} {surname}") # f strings are cooler than regular strings so make sure to use them when applicable
print("Please select from the list of items.\n")

print("----------------------------")
print("\tItems Available")
print("1 = Book")
print("2 = Ruler")
print("3 = Pen")
print("----------------------------")
shoppingItem = int(input("\nEnter the number of the item you would like: "))

if shoppingItem == 1:
    print("You bought a book")
elif shoppingItem == 2:
    print("You bought a ruler")
elif shoppingItem == 3:
    print("You bought a pen")
else:
    print("Invalid choice. Goodbye")

