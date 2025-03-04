def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

n = int(input("Enter n: "))
sum = 0
temp = n
digit_count = count_digits(n)
while temp > 0:
    digit = temp % 10
    sum += digit ** digit_count
    temp //= 10

if n == sum:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")

