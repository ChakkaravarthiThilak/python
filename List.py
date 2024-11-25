l=[1,2,3,4,5]
f=open("C:/Users/csc/Desktop/thilak/list.txt","bw")
for i in l:
    s=str(i)+'\n'
    a=s.encode()
    f.write(a)
f.close()
    
    
