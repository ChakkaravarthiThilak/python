class ari:
    def add(self,n1,n2):
        return n1+n2
    def sub(self,n1,n2):
        return n1-n2
    def multi(self,n1,n2):
        return n1*n2
    def div(self,n1,n2):
        return n1/n2
class ira(ari):
    def var(n1,n2):
        return n1,n2
x=ira()
a=int(input("Enter Your Choice"))
n1=int(input("Enter Your number"))
n2=int(input("Enter Your number"))
if a==1:
     print (x.add(n1,n2))
elif a==2:
     print (x.sub(n1,n2))
elif a==3:
     print (x.multi(n1,n2))
elif a==4:
     print (x.div(n1,n2))


