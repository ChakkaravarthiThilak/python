class mother:
    def __init__(self,name):
        self.name=name
    def var (self):
        print (self.name)
class father:
    def __init__(self,name):
        self.name=name
    def var (self):
        print (self.name)
class son:
    def __init__(self,name):
        self.name=name
    def var (self):
        print (self.name)
m=mother ("vasanthi")
f=father ("nagarajan")
s=son ("thilak")
for i in (m,f,s):
    i.var()
