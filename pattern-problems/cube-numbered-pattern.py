n = int(input('Enter size of cube:'))
m = n

# To calculate each output, we will calculate the distance to each
# of the sides, then pick the smallest distance and subtract it from n
for i in range(n*2-1):
    for j in range(m*2-1):
        top = i
        left = j
        bottom = 2*n - i - 2
        right = 2*m - j - 2
        print(n - min(top,left,bottom,right), end=" ")
    print()