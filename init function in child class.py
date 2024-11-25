class person:
    def __init__(self,name):
        self.name=name
    def var(self):
        print(self.name)
class stu(person):
    def __init__(self,name):
        person .__init__(self,name)
x=stu("Thilak")
x.var()
