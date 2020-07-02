'''
# BUBBLE SORT
from array import *
x = array('i', [])
print('How many elements = ', end='')
n = int(input())

for i in range(n):
    print('Enter elements = ', end='')
    x.append(int(input()))
print('Original array = ', x)

flag = False
for i in range(n-1):
    for j in range(n-1-i):
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
            flag = True
    if flag == False:
        break
    else:
        flag = False
print('Sorted array = ', x)


# LINEAR SEARCH
from array import *
x = array('i', [])
print('How many elements = ')
n = int(input())
for i in range(n):
    print('Enter elements = ', end=' ')
    x.append(int(input()))
#print('Original array = ', x)
lst = x.tolist()
print('List = ', lst)

print('Element to be searched = ')
s = int(input())
flag = False
for i in range(len(x)):
    if s == x[i]:
            print('Found at = ', i+1)
if flag == False:
    print('Not found')
'''

# SEARCH USING index()
from array import *
x = array('i', [])
print('How many = ', end='')
n = int(input())

for i in range(n):
    print('Enter elements = ', end=' ')
    x.append(int(input()))
lst = x.tolist()
print('original list', lst)
print('Enter element to be searched = ', end='')
s = int(input())
try:
    pos = x.index(s)
    print('Found at =', pos+1)
except Exception as e:
    print('Not Found')
print('THANKYOU')