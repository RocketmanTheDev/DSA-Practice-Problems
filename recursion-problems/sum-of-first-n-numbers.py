def sum_of_first_n_numbers(n):
    if n == 1:
        return 1
    return n + sum_of_first_n_numbers(n - 1)

print("Sum of first n numbers:", sum_of_first_n_numbers(int(input("Enter n: "))))  # 15