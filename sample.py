from array import *
arr = array('i',[])
n = int(input("Enter the array size"))
for i in range(n):
    x = int(input("Enter the element"))
    arr.append(x)

for e in range(n):
    print(arr[e])