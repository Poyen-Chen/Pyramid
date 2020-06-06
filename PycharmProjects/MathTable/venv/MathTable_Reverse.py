# 印出99乘法表--反向

count = 9

while count >= 2:
  FrontNumber = 9

  while FrontNumber >= 2:

    Result = FrontNumber * count
    print('%d*%d=%2d   ' %(FrontNumber, count, Result), end="")
    FrontNumber -= 1
  count -= 1
  print("\n")