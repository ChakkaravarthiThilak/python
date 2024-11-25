a=["C:/Users/csc/Desktop/thilak/file.txt","C:/Users/csc/Desktop/thilak/file2.txt"]
with open("C:/Users/csc/Desktop/thilak/file3.txt","w")as f1:
    for i in a:
        with open(i) as f2:
            f1.write(f2.read())
