with open("C:/Users/csc/Desktop/thilak/file.txt","r") as f1, open("C:/Users/csc/Desktop/thilak/file1.txt","a") as f2:
    for i in f1:
        print(i)
        f2.write(i)
    
