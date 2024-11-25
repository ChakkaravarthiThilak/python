import pickle
a=open("C:/Users/csc/Desktop/thilak/student.dat","br")
b=list(pickle.load(a))
print(b)
a.close()


       
