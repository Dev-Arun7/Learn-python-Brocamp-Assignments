#Selection Sort!!!!!
import array
size=int(input("Enter the size of array : "))
a=array.array("i")
print("Enter the values of array : ")
for i in range(size):
    value=int(input())
    a.append(value)
for i in range(size):
    j=i+1
    for j in range(size):
        if a[i]>=a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
        
            
        
   
        
    