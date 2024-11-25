class mother:
    def __init__(self,name):
        self.name=name
    def var(self):
        print(self.name)
class father:
     def __init__(self,name):
        self.name=name
     def var(self):
        print(self.name)
class son:
     def __init__(self,name):
        self.name=name
     def var(self):
        print(self.name)
a=mother('vasanthi')
b=father('Nagarajan')
c=son('Thilak')
for i in (a,b,c):
    i.var()
    
