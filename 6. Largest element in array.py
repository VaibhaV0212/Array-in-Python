'''
STEP 1: Declare and initialize an array.
STEP 2: Store first element in variable max.
STEP 3: Loop through the array from 0 to length of the array and compare the value of max with elements of the array.
STEP 4: If any element is greater than max, max will hold the value of that element.
STEP 5: At last, max will hold the largest element in the array.

from array import *
a = [54,2,3,4,5]
max = a[0]
for i in range(0, len(a)):
    if a[i] > max:
        max = a[i]
print(max)
'''

x = []
print('How many elements = ', end='')
n = int(input())

for i in range(n):
    print('Enter elements = ', end='')
    x.append(int(input()))

print('Original list = ', x)

big = x[0]
small = x[0]
for i in range(1, n):
    if x[i] > big:
        big = x[i]
    if x[i] < small:
        small = x[i]

print("Maximum is = ", big)
print("Minimum is = ", small)