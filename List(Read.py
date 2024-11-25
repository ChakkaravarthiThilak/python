l=[ ]
f=open("C:/Users/csc/Desktop/thilak/list.txt","br")
for i in f:
    x=int(i)
    l=l+[x]
print(l)
f.close()
       
