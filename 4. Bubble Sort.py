from array import *

x = array('i', [])
print('How many elements = ',end=' ')
n = int(input())

for i in range(n):
    print('Enter Elements = ',end=' ')
    x.append(int(input()))

print('Original array = ',x)

#bubble sort
flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if x[j] > x[j+1]:
            t = x[j]
            x[j] = x[j+1]
            x[j+1] = t
            flag= True
    if flag== False:          #no swapping means array is in sorted order
        break
    else:
        flag=False

print('Sorted array is = ', x)