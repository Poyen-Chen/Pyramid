# Print out 9*9 multiplication table with pyramid pattern

for i in range(1,10):
    for k in range(1,10-i):
        print(end="       ")                                 # 7 Space of left side
    for j in range(1,i+1):
        print("%d*%d=%2d" %(i, j, i*j), end="        ")     # 8 Space of middle and right side
    print("")