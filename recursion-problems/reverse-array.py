def reverse_array(arr):
    if len(arr) == 0:
        return []
    return [arr[-1]] + reverse_array(arr[:-1])

print("Enter the array elements separated by a space: ")
arr = input().split()
print(reverse_array(arr))