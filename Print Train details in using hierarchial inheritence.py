class train:
    def __init__(self,number,name,destination):
        self.num=number
        self.name=name
        self.des=destination
    def print (self):
        print(self.num)
        print(self.name)
        print(self.des)
class passenger (train):
    def __init__(self,number,name,destination,coach):
        train .__init__(self,number,name,destination)
        self.coach=coach
    def print(self):
        super().print()
        print (self.coach)
class seat(train):
    def __init__(self,number,name,destination,seat):
        train .__init__(self,number,name,destination)
        self.seat=seat
    def print(self):
        super().print()
        print(self.seat)
x=passenger(1234,"ajai","comibatore","s1")
print("passenger details")
x.print()
y=seat(1234,"Thilak","comibatore",34)
print("passenger details")
y.print()
