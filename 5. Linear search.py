from array import *
x = array('i',[])
print("How many elements = ",end='')
n = int(input())

for i in range(n):
    print("Enter elements = ",end='')
    x.append(int(input()))

print("Original array = ",x)

#Linear sort
print("Find the element to search = ", end=' ')
s = int(input())
flag = False
for i in range(len(x)):
    if s == x[i]:
        print("Found at position = ",i+1)
        flag = True
if flag == False:
    print('Not found')