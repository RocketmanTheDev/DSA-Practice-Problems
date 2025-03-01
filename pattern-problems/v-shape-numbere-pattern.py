n = int(input('Enter size of shape:'))
m = 1

for i in range(n):
    for j in range(m):
        print(j+1, end="")
    for k in range((n-i-1)*2):
        print(" ", end="")
    for j in range(m):
        print(i-j+1, end="")
    m+=1
    print()