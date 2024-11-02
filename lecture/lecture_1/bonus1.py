#Packages
import numpy as np

amin = int(input("Enter the minimum value: "))
amax = int(input("Enter the maximum value: "))

# Method 1
total = 0
for i in range(amin, amax+1):
    total += i
print(f'Method 1: Summation from {amin} to {amax} = {total}')

# Method 2

result = np.sum(np.array(range(amin, amax+1)))
print(f'Method 2: Summation from {amin} to {amax} = {result}')