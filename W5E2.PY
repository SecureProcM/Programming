diviend = int(input("Enter the dividend:"))
divisor = int(input("Enter the divisor: "))
remainder = diviend % divisor
integer_divison = diviend // divisor
float_division = diviend / divisor

print(f"The Remainder when {remainder} is divided by {divisor} is {remainder} ")
print(f"The integer division when {diviend} is divided by {divisor} is {integer_divison}")
print(f"The float division when {diviend} is divided by {divisor} is {float_division} ")
