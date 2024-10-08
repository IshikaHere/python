#using while loop take first input as which multiplication table we want to print and second input wwill be number for rows

n = int(input("multiplication table  "))
m = int(input("number of rows: "))

i = 1
while i <= m:
  print(n, "*", i, "=", n * i)
  i += 1
