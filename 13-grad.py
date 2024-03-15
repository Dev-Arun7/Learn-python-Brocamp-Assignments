print("Enter the mark scored by the sutdent !! \n")
w=int(input("Written test : "))
l=int(input("Lab exames : "))
a=int(input("Assignments : "))

grade=(w * 70)/100 + (l * 20)/100 + (a*10)/100
print("Grade of the student is "+str(grade))
