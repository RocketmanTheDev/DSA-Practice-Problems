n = int(input('Enter size of triangle:'))
m = n

for i in range(n):
    for j in range(m):
        print(j+1, end="")
    m-=1
    print()