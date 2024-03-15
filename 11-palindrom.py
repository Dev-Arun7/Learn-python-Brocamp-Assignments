s=str(input("Enter the String : "))
l=len(s)
for i in range (l):
    if s[i]==s[l-i-1]:
       flag=1
    else:
        flag=0
        break
if flag==1:
    print("palindrome")
else:
    print("String is not palindrom")