n = int(input('Enter size of triangle:'))
m = 1

for i in range(n):
    for j in range(n - int(m/2)- 1):
        print(" ", end="")
    for k in range(m):
        print("*", end="")
    for l in range(n - int(m/2)- 1):
        print(" ", end="")
    m+=2
    print()