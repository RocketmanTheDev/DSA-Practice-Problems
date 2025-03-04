def print_1_to_n(i, n):
    if i>n:
        return
    print(i)
    print_1_to_n(i + 1, n)

n = int(input("Enter n: "))
print_1_to_n(1, n)
