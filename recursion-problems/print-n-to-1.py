def print_n_to_1(i, n):
    if i<1:
        return
    print(i)
    print_n_to_1(i - 1, n)

n = int(input("Enter n: "))
print_n_to_1(n, n)
