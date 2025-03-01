n = int(input('Enter size of diamond:'))
m = n*2-1

for i in range(n):
    for j in range(n - int(m/2)):
        print("*", end="")
    for k in range(m-1):
        print(" ", end="")
    for l in range(n - int(m/2)):
        print("*", end="")
    m-=2
    print()

m = 1
n-= 1

for i in range(n):
    for j in range(n - int(m/2)):
        print("*", end="")
    for k in range(m+1):
        print(" ", end="")
    for l in range(n - int(m/2)):
        print("*", end="")
    m+=2
    print()

