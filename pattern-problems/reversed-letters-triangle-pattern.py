n = int(input('Enter size of triangle:'))
m = 1

for i in range(n):
    for j in range(m):
        print(chr(n-m+j+(ord('A'))), end=" ")
    m+=1
    print()