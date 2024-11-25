class person:
    def __init__(self,name):
        self.name=name
    def var(self):
        print(self.name)
class stu(person):
    def __init__(self,name):
        super().__init__(name)
        self.year=2000
x=stu("Thilak")
print(x.year)
x.var()
