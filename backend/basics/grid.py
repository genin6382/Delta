n = int(input("enter"))

for i in range(n*2-1):
  if i%2 == 0:
    for j in range(n-1):
       print("  |", end="")
  else:
    for k in range(n):
      print("-- ",end="")
  print()