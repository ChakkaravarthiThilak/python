a=6
for i in range (a):
    n=1
    for j in range (a,0,-1):
        if j>i:
            print(" ",end=" ")
        else:
            print(n,end=" ")
            n+=1
    print()
