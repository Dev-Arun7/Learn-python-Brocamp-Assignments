d=7
f=8
for i in range(1,5):
    for j in range(1, 6-i):
            print(d,end=" ")
            d=d+1
    d=d-1
    f=f-2
    d=d-f
    print()
    