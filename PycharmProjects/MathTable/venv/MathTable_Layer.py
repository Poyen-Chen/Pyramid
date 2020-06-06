# 首先將九九乘法表一邊數字1~9間距離視為16單位長,且另一邊Y軸也16單位長,則繞著4邊走可圍成一個16*16方形
# 現在請向內縮建構類似方形3次,其邊長依序為12,8,4單位長
# Form multi-layers matrix

for i in range(1,10):
    for j in range(1,10):
        if i == 7 and j <= 3:
            print(end="       ")    # Space of column
        elif j == 3 and i >= 7:
            print(end="       ")  # Space of column
        elif i == 4 and j <= 6:
            print(end="       ")
        elif j == 6 and i >= 5:
            print(end="       ")
        elif i == 2 and j <= 8:
            print(end="       ")
        elif j == 8 and i >= 3:
            print(end="       ")
        else:
            print("%d*%d=%2d " %(i, j, i*j), end="")
    print("")
