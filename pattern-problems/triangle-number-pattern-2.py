n = int(input('Enter size of triangle:'))
m = 1

for i in range(n):
    for j in range(m):
        print(i+1, end="")
    m+=1
    print()