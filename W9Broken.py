# W9Broken.py
#The program contains 3 logical and syntax errors. Fix these errors.  
# For your reference, the program attempts to process a list of numbers. 
# The goal is to:
#1.	Double each even number in the list.
#2.	Add 5 to each odd number.
#3.	Print the modified list after each transformation.

# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Loop to double each even number
for num in range(len(numbers)): # missing the range and the length
    if numbers[num] % 2 == 0:
        numbers[num] = numbers[num] * 2 # missing num
print("List after doubling even numbers:", numbers)

# Loop to add 5 to each odd number
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] += 5
print("List after adding 5 to odd numbers:", numbers)
