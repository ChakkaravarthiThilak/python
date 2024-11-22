class calc():
    def add (self,n1,n2):
        return(n1+n2)
    def sub (self,n1,n2):
        return(n1-n2)
    def multi (self,n1,n2):
        return(n1*n2)
    def div (self,n1,n2):
        return(n1/n2)
c=calc()
a=int(input("Enter your choice"))
n1=int(input("Enter your number"))
n2=int(input("Enter your number"))
if a==1:
       print(c.add(n1,n2))
elif a==2:
    print (c.sub(n1,n2))
elif a==3:
    print (c.multi(n1,n2))
elif a==4:
    print (c.div(n1,n2))
else:
    print(nothing)
