class parents:
    def __init__(self):
        self.a=2
class child (parents):
    def __init__(self):
        parents .__init__(self)
        print(self.a)
        self.a=3
        print(self.a)
x=child()
y=parents()
print(x.a)
print(y.a)
