class student:
    def __init__(self,name,i_d,mark1,mark2,mark3):
        self.name=name
        self.i_d=i_d
        self.m1=mark1
        self.m2=mark2
        self.m3=mark3
    def var(self):
        self.total=(self.m1+self.m2+self.m3)
        self.avg=(self.total/3)
    def abc(self):
        print(self.name)
        print(self.i_d)
        print(self.m1)
        print(self.m2)
        print(self.m3)
        print(self.total)
        print(self.avg)
s1=student("Thilak",9509,70,80,85)
s1.var()
s1.abc()
