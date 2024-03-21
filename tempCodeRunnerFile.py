
from array import *
marks = array('i',[6,3,7,1,9])
print(marks)
for j in marks:
    print(j)

print("Copied Array is: ")   
newArr = array(marks.typecode,(a for a in marks))
for e in newArr:
    print(e)


