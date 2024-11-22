class person:
    def __init__(self,r):
        self.b=r
    def var(self):
        print(2*3.14*self.b)
    def abc(self):
        print(3.14*self.b**2)
r=int(input("Enter a number"))
p=person(r)
p.var()
p.abc()
