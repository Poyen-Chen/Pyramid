# Print out 9*9 multiplication table with 3 by 3 matrix (9宮格)

for i in range(2,10):
    if i == 4:
        for k in range(1,10):
            print(end="")               # Space of row
    elif i == 7:
        for k in range(1,10):
            print(end="")              # Space of row
    else:
        for j in range(2,10):
            if j == 4:
                print(end="      ")    # Space of column
            elif j == 7:
                print(end="      ")    # Space of column
            else:
                print("%d*%d=%2d " %(i, j, i*j), end="")
    print("")