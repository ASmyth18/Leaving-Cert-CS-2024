# Question 16(a)
# Examination Number: 129478

# Prompt the user to enter a password and store the ...
# value entered in the variable password
password = input("Enter a password: ")

# A variable to store all the lowercase letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # (ii) Had to add var for upper case letters

# The variables lowercase and uppercase indicate the presence or ...
# absence of lowercase and uppercase characters in the password
lowercase = False # True if password contains a lowercase letter
uppercase = False # True if password contains an uppercase letter
contains_digit = False # (iv) True if password contains a digit
first_digit = False  # (vi) True if the first character of the password is a digit
last_digit = False  # (vi) True if the last character of the password is a digit
only_digits = True # (vii) True if the password only contains digits

# Loop through each character in the password and ...
# check the password for specific characters
for index, character in enumerate(password): # (vi)
    if character in LOWER_CASE_LETTERS:
        lowercase = True
        only_digits = False
    if character in UPPER_CASE_LETTERS:
        uppercase = True
        only_digits = False
    if character.isdigit():
        contains_digit = True
        # (vi)
        if index == 0:
            first_digit = True
        elif index == len(password) - 1:
            last_digit = True
    else:
        only_digits = False

# Calculate the score based on the rules
# (i) Initialise score
score = 0

# Rule 1
password_length = len(password)
if password_length > 7:
    score += 5
elif 4 <= password_length <= 7:
    score += 2
else:
    score -= 2

# Rule 2
if lowercase:
    score = score + 1

# Rule 3
if lowercase and uppercase:
    score = score + 5

# (iii) Rule 4
if uppercase:
    score = score + 2
    
# (iv) Rule 5
if contains_digit:
    score = score + 5

# (vi) Rule 6
if first_digit:
    score = score + 1
if last_digit:
    score = score + 1
if first_digit and last_digit:
    score = score + 2
    
# (vii) Rule 7
if only_digits:
    score = score - 10


# Display the score
print(score)