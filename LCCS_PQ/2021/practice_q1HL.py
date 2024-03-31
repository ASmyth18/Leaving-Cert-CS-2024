# Question 16(a)
# Examination Number: 129478

# This docstring contains an optimised version of the code because the way they want you to do it is bad
"""
def is_anagram(w1, w2):
    return sorted(w1.replace(" ", "").lower()) == sorted(w2.replace(" ", "").lower())

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
phrase = input("Enter a phrase: ")

print(f"{word1} is {'an' if is_anagram(word1, word2) else 'NOT an'} anagram of {word2}")
print(f"{word1} is {'an' if is_anagram(word1, word2) else 'NOT an'} anagram of {word2}")

print(f"{word1} is {'an' if is_anagram(word1, phrase) else 'NOT an'} anagram of the phrase '{phrase}'")
print(f"{word2} is {'an' if is_anagram(word2, phrase) else 'NOT an'} anagram of the phrase '{phrase}'")
"""

# function definition used in part (v)
def is_anagram(w1, w2):
    w1 = w1.replace(" ", "").lower()  # Remove spaces and convert to lowercase as a part of (VI)
    w2 = w2.replace(" ", "").lower()
    if sorted(w1) == sorted(w2):
        return True
    else:
        return False

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ") # (i) Had to add user input for word2
phrase = input("Enter a phrase: ") # (VI)

# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
if (sorted(word1) == sorted(word2)):
    print(f"{word1} is an anagram of {word2}") # (ii) Asked to display "is an anagram of"#
else:
    print(f"{word1} is NOT an anagram of {word2}") # (iii) If the words are not an anagram, asked to display "is NOT an anagram of"

if is_anagram(word1, word2): # (V) Asked to extend the code so that it checks the words twice, once using the original if else block and another using the function
    print(f"{word1} is an anagram of {word2}")
else:
 print(f"{word1} is NOT an anagram of {word2}")
 
# (VI) Code to handle the phrases anagram detection as dictated by part vi 
if is_anagram(word1, phrase):
    print(f"{word1} is an anagram of the phrase '{phrase}'")
else:
    print(f"{word1} is NOT an anagram of the phrase '{phrase}'")

if is_anagram(word2, phrase):
    print(f"{word2} is an anagram of the phrase '{phrase}'") 
else:
    print(f"{word2} is NOT an anagram of the phrase '{phrase}'")
