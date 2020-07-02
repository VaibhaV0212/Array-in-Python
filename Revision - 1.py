# 1
from array import *
arr = array('u', ['i', 'L', 'u'])   # u = unicode
print('The array elements are = ')
for i in arr:
    print(i)
print()

# 2
x = array('i', [4, 5, 6, 2, 1, 9])
for i in x[1:4]:
    print(i)
print()

# 3
arr = array('i', [1, 2, 3, 4, 5])
print('Original array is = ', arr)

arr.append(6)
print(arr)
arr.insert(0, 0)
print(arr)
arr.remove(4)
print(arr)
arr.pop()
print(arr)
arr.pop(1)
print(arr)
n = arr.index(3)
print(n)
lst = arr.tolist()
print('List = ', lst)
print('Array = ', arr)