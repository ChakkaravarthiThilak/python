class mother:
    mothername=" "
    def mother(self):
        print(self.mothername)
class father:
    fathername=" "
    def father(self):
        print(self.fathername)
class son(mother,father):
    def parents(self):
        print("mother:",self.mothername)
        print("father:",self.fathername)
x=son()
x.fathername="Ram"
x.mothername="sita"
x.parents()
