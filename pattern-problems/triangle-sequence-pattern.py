n = int(input('Enter size of triangle:'))
m = 1
output = 1

for i in range(n):
    for j in range(m):
        print(output, end=" ")
        output+=1
    m+=1
    print()