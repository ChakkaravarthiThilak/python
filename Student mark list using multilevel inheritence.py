class mark:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
class total (mark):
    def __init__(self,m1,m2,m3):
        mark.__init__(self,m1,m2,m3)
    def calc(self):
        self.total=self.m1+self.m2+self.m3
class average(total):
       def __init__(self,m1,m2,m3):
           total.__init__(self,m1,m2,m3)
       def calc2(self):
           self.average=self.total/3
       def var(self):
           print(self.total)
           print(self.average)
x=average(90,80,70)
x.calc()
x.calc2()
x.var()
