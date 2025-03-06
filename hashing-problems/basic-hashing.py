# TASK:
# Given an array of integers: [1, 2, 1, 3, 2] and we are given some queries: [1, 3, 4, 2, 10].
# For each query, we need to find out how many times the number appears in the array.
# For example, if the query is 1 our answer would be 2, and if the query is 4 the answer will be 0.

arr_size = int(input("Enter the size of the array: "))
array = []

# Read the array elements
for i in range(arr_size):
    array.append(int(input(f"Enter element {i+1}: ")))

# Create a frequency dictionary
hash_array = {}

for num in array:
    hash_array[num] = hash_array.get(num, 0) + 1

query_size = int(input("Enter the size of the query: "))

# Process queries
for i in range(query_size):
    query = int(input(f"Enter query {i+1}: "))
    print(hash_array.get(query, 0))  # Default to 0 if query is not found

