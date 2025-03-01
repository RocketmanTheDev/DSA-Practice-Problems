n = int(input('Enter size of frame:'))
m = n

for i in range(n):
    for j in range(m):
        if j==0 or i==0 or j == (m - 1) or i == (n - 1): print("*", end="")
        else : print(" ", end="")
    print()