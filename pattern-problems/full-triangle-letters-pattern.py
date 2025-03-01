n = int(input('Enter size of triangle:'))
m = 1

for i in range(n):
    for j in range(n - int(m/2)- 1):
        print(" ", end="")
    # Below the math can get confusing, in essence to express the triangle,
    # I separate it into two smaller ones - the one up to the middle,
    # An the second one which I need to calculate in reverse - hence the complicated math there
    for k in range(int(m/2)):
        print(chr(k+ord('A')), end="")
    for p in range(int(m/2-1)):
        print(chr(int(m/2-p-2)+ord('A')), end="")
    for l in range(n - int(m/2)- 1):
        print(" ", end="")
    m+=2
    print()