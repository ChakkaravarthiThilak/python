class name:
    name=" "
    def name (self):
        print(self.name)
class age:
    age=" "
    def age (self):
        print(self.age)
class i_d(name,age):
    i_d=" "
    def i_d(self):
        print(self.i_d)
    def student(self):
        print("name:",self.name)
        print("age:",self.age)
x=i_d()
x.name="Thilak"
x.age="24"
x.student()
