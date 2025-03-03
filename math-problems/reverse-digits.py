n = int(input("Enter n:"))

print("Reverse of ", n, " is: ", end="")
while n > 0:
    print(n % 10, end="")
    n = n // 10