COUNT = 11

for x in range(1, COUNT + 1):
  for y in range(x):
    print("*", end="")
  print("")

print("")

for x in range(COUNT, 0, -1):
  for y in range(COUNT - x):
    print(" ", end="")
  for y in range(x):
    print("*", end="")
  print("")