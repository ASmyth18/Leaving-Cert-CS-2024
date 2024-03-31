# Question 16 (a)
# Examination Number: 129478

"""
Throughout this code you can see empty print statements like this:
print()
The reason for this is due to the built in \n of the print statement, as seen below,
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Thus print naturally has a new line component built in which is applied to the end of a string,
In the case of an empty print statement it is applied to an empty line thus providing us with a line break.
"""

from random import randint

print("Dice simulation program and analysis program") # (i) added "and analysis program"
results = []
frequencies = [0, 0, 0, 0, 0, 0]

# Loop 100 times
for i in range (100):
    throw_result = randint(1,6) # store a random value between 1 and 6
    results.append(throw_result) # append each value to results

    # Start to build up a list of frequencies for each value thrown
    # (iii) Had to complete this if else block to account for throw results 3 through 6
    if throw_result == 1:
      frequencies[0] = frequencies[0] + 1
    elif throw_result == 2:
      frequencies[1] = frequencies[1] + 1
    elif throw_result == 3:
      frequencies[2] = frequencies[2] + 1
    elif throw_result == 4:
      frequencies[3] = frequencies[3] + 1
    elif throw_result == 5:
      frequencies[4] = frequencies[4] + 1      
    elif throw_result == 6:
      frequencies[5] = frequencies[5] + 1      
      

print()
# print("Results:", results) # (iv) Asked to comment out this line
# print("Frequencies:", frequencies) # (ii) added this line

# (V) Had to display in tabular format
print("Dice\tFrequency")
print("-------------------")

# (VI) Had to determine the number with the highest freq and print
max_frequency = max(frequencies)
most_often_rolled = frequencies.index(max_frequency) + 1

for i in range(len(frequencies)):
    print(f"{i + 1}\t{frequencies[i]}")
    
# (VI) Prints the most often rolled number   
print()
print(f"The number {most_often_rolled} was rolled most often ({max_frequency} times).")

# (VII) Had to add a horizontal bar chart of asterisks to represent the frequency of each result
print()
for freq in frequencies:
    print("*" * freq)

    