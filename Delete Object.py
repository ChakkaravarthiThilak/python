class person:
    def __init__(self,fname,lname):
        self.a=fname
        self.b=lname
    def var(self):
        print(self.a,self.b)
p=person("Hari","Sasi")
p.var()
del p.lname
#print(p.lname)
p.var()
