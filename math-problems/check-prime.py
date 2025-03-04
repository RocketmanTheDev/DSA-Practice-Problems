from math import sqrt

n = int(input("Enter n: "))
divisors = []

for i in range(1, int(sqrt(n)+1)):
    if n % i == 0:
        divisors.append(i)
        if i != n // i:
            divisors.append(n // i)

if len(divisors) == 2:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")