# Print out 9*9 multiplication table with diamond pattern

for i in range(1,10):
    if i <= 5:
       for k in range(1,10-i):
           print(end="       ")                                 # 7 Space of left side
    else:
        for k in range(1,i):
           print(end="       ")
    if i <= 5:
       for j in range(1,i+1):
           print("%d*%d=%2d" %(i, j, i*j), end="        ")     # 8 Space of middle and right side
    else:
       for j in range(1, 11-i):
           print("%d*%d=%2d" %(i, j, i*j), end="        ")
    print("")
