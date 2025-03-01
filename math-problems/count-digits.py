import math

n = int(input('Enter n:'))
print("This number has: ", end="")
result = math.floor(math.log10(n))+1
if result == 1 : print(result, end=" digit.")
else: print(result, end=" digits.")