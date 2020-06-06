# Print pyramid with star
# Method 1

def pattern(n):
  k = 2*n-2
  for i in range(0,n):               # Number of Row
      for j in range(0,k):           # Number of space in each row
           print(end=" ")                 # Control the pattern
      k = k-1                        # Decrease the space of each row
      for j in range(0,i+1):         # Number of star
          print("*", end=" ")            # Control the pattern
      print(" ")

pattern(5)


# Method 2
n = int(input("enter n value:"))
for i in range(n):
    print(' '*(n-i-1)+' *'*(i+1))




