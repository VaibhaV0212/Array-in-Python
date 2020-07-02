'''
Input : arr[] = {1, 2, 3}
Output : 6
1 + 2 + 3 = 6

Input : arr[] = {15, 12, 13, 10}
Output : 50
'''

'''
from array import *
x = array('i',[])
#n = int(input())

for i in range(0,len(x)):
    print("Enter elements = ", end=' ')
    x.append(int(input()))

sum = 0
for i in range(0,len(x)):
    for j in range(0,len(x)-1-i):
        sum = x[0]+x[1]
        sum+=1

print(x)
'''

from array import *
arr = [1,2,3,4]
sum = 0
for i in range(0,len(arr)):
    sum = sum + arr[i]

print('Sum is', sum)

