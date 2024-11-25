class a:
    def add (self,n1,n2):
        return n1+n2
class b(a):
    def add (self,n1,n2):
        return n1+n2
y=b()
n1=30
n2=20
r=y.add(n1,n2)
print(r)
