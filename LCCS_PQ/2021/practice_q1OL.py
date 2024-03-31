# Question 16(a)
# Examination Number: 129478

pin = "1579"
loggedIn = False # (iii) Asked to create a boolean initially set to false
failedAttempts = 0 # (VI) Asked to create a variable that tracks failed attempts

# (i) Added comment explaining input line
# This line prompts the user to enter a PIN and stores the input value in the variable userTry
userTry = input("Enter PIN:")

while loggedIn == False: # (V) Asked to put the code into a While  
    if userTry == pin:
        loggedIn = True # (IV) Asked to amend the program so that the boolean is set to true upon correct entry of the PIN
        print("Welcome")
    elif failedAttempts >= 2: # (VII) Only allowed 3 incorrect attempts before programme breaks
        print(f"You have entered the pin incorrectly {failedAttempts} times")
        break
    else:
        print("Incorrect PIN") # (ii) Asked to amend the program so that "Incorrect PIN" is displayed if the input is wrong
        failedAttempts = failedAttempts + 1
        userTry = input("Enter PIN:")
    
