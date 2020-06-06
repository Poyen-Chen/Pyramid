# Print out 9*9 multiplication table with "while" loop

count = 2

while count <= 9:
  FrontNumber = 2

  while FrontNumber <= 9:

    Result = FrontNumber * count
    print('%d*%d=%2d    ' %(FrontNumber, count, Result), end="")
    FrontNumber += 1
  count += 1
  print("\n")



# Print out 9*9 multiplication table with "for" loop

for i in range(2,10):
    for j in range(2,10):
        s=  i*j
        print ('%d*%d=%2d   ' %(i, j, s), end="")

    print('\n')



