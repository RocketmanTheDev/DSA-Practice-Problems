def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of n:", factorial(int(input("Enter n: "))))  # 15