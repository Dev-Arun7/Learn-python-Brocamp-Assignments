#insertion Sort
import array
size=int(input("Enter the size of array : "))
print("Enter the elements : ")
a=array.array('i')
for i in range(size):
    value=int(input())
    a.append(value)
for i in range(size):
    for j in range(size-1):
        if a[j]<=a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)
    