def fibonacci(n):
    if n <=1 :
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Enter the length of the series: ")
n = int(input())
print("Fibonacci Series: ")
i=0
while fibonacci(i) <= n:
    print(fibonacci(i), end=" ")
    i+=1