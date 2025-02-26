# W4Broken.py

# The following Python program is supposed to calculate 
# various mathematical expressions, but it doesn't work 
# correctly because of operator precedence issues. 
# Fix the code so the calculations are performed in the 
# correct order.

# 1. Calculate the average of three numbers
# problem wasnt divide by 3
# i added the /3 to the question
# also added brackets to the numbers
num1 = 5
num2 = 10
num3 = 15
average = (num1 + num2 + num3 / 3)
print("The average is:", average)

# 2. Calculate the perimeter of a rectangle with length and width
# problem was that it wasnt times by 2
# i added 2 *  
length = 10
width = 5
perimeter = 2 * (length + width)
print("The perimeter of the rectangle is:", perimeter)

# 3. Calculate the area of a trapezoid
# the area has been multiplyed
# i added  0.5 * to the question
base1 = 10
base2 = 20
height = 5
area = 0.5 * (base1 + base2) * height 
print("The area of the trapezoid is:", area)

