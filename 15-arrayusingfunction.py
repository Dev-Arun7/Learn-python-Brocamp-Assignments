import array
myarray=array.array('i')
def getarray():
    size=int(input("Enter the size of array : "))
    print("Enter the values of array : ")
    for i in range(size):
        value=int(input())
        myarray.append(value)
    return myarray,size
def displayarray(a,size):
    print("your array is : ", end=" ")
    for i in range(size):
        print(a[i],end=" ")

a,b=getarray()
displayarray(a,b)
    