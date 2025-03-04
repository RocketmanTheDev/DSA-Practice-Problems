n = int(input("Enter n: "))

front = n
rev = 0
while front > 0:
    rev = rev * 10 + front % 10
    front = front // 10

if rev == n:
    print(n, "is a palindrome.")
else:
    print(n, "is not a palindrome.")
