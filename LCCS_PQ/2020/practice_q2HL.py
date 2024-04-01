# Question 16(b)
# Examination Number: 129478

# A variable to store all the lower case letters in the alphabet
LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"

def calculate_score(password):

    # The variables lowercase and uppercase indicate the presence or
    # absence of lowercase and uppercase characters in the password
    lowercase = False #True if password contains a lowercase letter
    uppercase = False #True if password contains an uppercase letter

    # Loop through each character in the password and ...
    # ... check the password for specific characters
    for character in password:
        if character in LOWER_CASE_LETTERS:
            lowercase = True
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True

    # Calculate the score based on the rules

    score = 0

    # Rule 1
    if len(password) > 7:
        score = score + 5

    # Rule 2
    if lowercase:
        score = score + 1

    # Rule 3
    if lowercase and uppercase:
        score = score + 5

    return score

"""
Funnily enough, this entire function can be a singular line of code if you really want it to be and it still satisfies the requirements:

return len(password) > 7 and any(char in LOWER_CASE_LETTERS for char in password) and any(char in UPPER_CASE_LETTERS for char in password)

Of course, for this to work we have to initialise the variables elsewhere; nonetheless it's still quite funny.
"""
def is_strong(password): # (iv)
    # A variable to store all the lowercase letters in the alphabet
    LOWER_CASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
    
    # Variables to indicate the presence of lowercase and uppercase letters
    has_lowercase = False
    has_uppercase = False
    
    # Check for lowercase and uppercase letters in the password
    for char in password:
        if char in LOWER_CASE_LETTERS:
            has_lowercase = True
        elif char in LOWER_CASE_LETTERS.upper():
            has_uppercase = True
    
    # Check if the password meets the criteria for being strong
    if len(password) > 7 and has_lowercase and has_uppercase:
        return True
    else:
        return False


# Test driver
"""
(ii) I wasn't sure if they wanted you to simply replace the fourth index of the list manually or to use list operations
"""
test_passwords = ["sun", "Sun", "Sunshine", "12345", "123456789"]

# (iii)
weakest_password = None
weakest_score = float('inf')

test_passwords.pop(4)
test_passwords.insert(4,"Moonlight")
print("Score", "Password") # (i) Had to display in tabular format: ln 42-46
print("----- --------")
for password in test_passwords:
    pass_score = calculate_score(password)
    print(f"{pass_score:<5} {password}") # This is a more interesting way of putting in a tabular format: ":<5" means a padding of 5 spaces to the right, ensures alignment
 
    # (iii) Determines weakest score and associating password
    if pass_score < weakest_score:
        weakest_score = pass_score
        weakest_password = password
print(f"\nThe weakest password is: {weakest_password} with a score of {weakest_score}")
print()

# (v) Tests strength of passwords in the test list
print("The strong passwords are:")
for password in test_passwords:
    if is_strong(password):
        print(password)
