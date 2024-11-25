a=["C:/Users/csc/Desktop/thilak/file.txt","C:/Users/csc/Desktop/thilak/file2.txt"]
f1=open("C:/Users/csc/Desktop/thilak/file3.txt","w")
for i in a:
    f2=open(i)
    f1.write(f2.read())
f1.close()
