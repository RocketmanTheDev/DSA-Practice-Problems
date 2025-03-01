n = int(input('Enter size of half diamond:'))
m = 1

for i in range(n):
    for j in range(m):
        print("*", end="")
    m+=1
    print()

m = n-1

for i in range(n):
    for j in range(m):
        print("*", end="")
    m -= 1
    print()
