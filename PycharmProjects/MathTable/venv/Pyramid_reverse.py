# Print reverse of pyramid with star
# Method 1

def reverse_pattern(n):
    k = 2*n-2
    for i in range(n,-1,-1):          # Number of row
        for j in range(k,0,-1):       # Number of space in each row
            print(end=" ")
        k = k+1                       # Increase the space of each row
        for j in range(0,i):          # Number of star
            print("*", end=" ")
        print("")

reverse_pattern(5)

# Method 2
n = int(input("enter n value:"))
for i in range(n):
    print(' '*(i+1)+' *'*(n-i))