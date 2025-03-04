def print_n_times(i, n):
    if i>n:
        return
    print("Hello, World!")
    print_n_times(i+1, n)

n = int(input("Enter n: "))
print_n_times(1, n)
