import array
size = int(input("Enter the size of Array1 : "))
print("enter the values of Array1 : ")
array1 = array.array('i')
for x in range(size):
    value = int(input(f""))
    array1.append(value)
array2 = array1
array2.append(int(input("Add a element into array2 : ")))
print ("Array1 : ",end="")
for i in range(size):
    print (" "+str(array1[i]),end="")
print("")
print("Array2 :", end="")
for i in range(size+1):
    print(" "+str(array2[i]), end="")
    

