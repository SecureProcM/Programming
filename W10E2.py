# Tell the user to enter the numbers of row
n = int(input("Enter the number of rows:"))
for i in range(1, n + 1):

 for j in range(1, i + 1):
  print(i * j, end= " ")
 print()
