import numpy as np
row=int(input("enter the rows number : "))
col=int(input("enter the coloumns number : "))
array1=np.zeros((row,col), dtype=int)
array2=np.zeros((row,col), dtype=int)
array3=np.zeros((row,col), dtype=int)
print("Enter the values of array1 : ")
for i in range(row):
    for j in range(col):
        value=int(input())
        array1[i][j]=value
print("Enter the values of array2 : ")
for i in range(row):
    for j in range(col):
        value2=int(input())
        array2[i][j]=value2
for i in range(row):
    for j in range(col):
        array3[i][j]=array1[i][j]+array2[i][j]
print("Sum of Two array is : ")
for i in range(row):
    for j in range(col):
        print(array3[i][j], end=" ")
    print("\n")
    