from array import *

M = int(input('Enter element M = '))
N = int(input('Enter element N = '))

if M > N:
    print(M - N)
else:
   print(N - M)


x = array('i', [])
print('How many elements = ',end=' ')
n = int(input())
for i in range(n):
    print('Enter Elements = ',end=' ')
    x.append(int(input()))

#print('Original array = ',x)

#bubble sort
sum = 0
big = 0
flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if x[j] > x[j+1]:
            t = x[j]
            x[j] = x[j+1]
            x[j+1] = t
            flag= True
            sum = sum + x[j]
    if flag== False:          #no swapping means array is in sorted order
        break
    else:
        flag=False
   # sum = sum + x[j]
print('Sorted array is = ', x)
print('Sum of array is = ', sum)