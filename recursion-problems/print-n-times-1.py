def print_n_times(n):
    if n == 0:
        return
    print("Hello, World!")
    print_n_times(n-1)

n = int(input("Enter n: "))
print_n_times(n)
