#Tell the user to enter a number to print the multiplication table
n = int(input("Enter a number and I'll print the multiplication table :"))
for i in range(1,  11):
 print(f"{n} x {i} = {n * i}")