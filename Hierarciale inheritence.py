class animal:
    def __init__(self,name):
        self.name=name
    def abc(self):
        pass
class dog(animal):
    def bark(self):
        print(self.name)
class cat(animal):
    def meow(self):
        print(self.name)
x=dog("Bubbloo")
y=cat("keo")
x.bark()
y.meow()
