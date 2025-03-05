def check_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return check_palindrome(s[1:-1])

print("Enter a string: ")
s = input()

if check_palindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
