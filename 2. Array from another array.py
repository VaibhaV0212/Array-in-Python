from array import *
arr1 = array('i', [2, 3, 4, 45])
arr2 = array(arr1.typecode, (a for a in arr1))
for i in arr2:
    print(i)