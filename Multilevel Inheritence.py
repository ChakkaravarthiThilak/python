class grandfather:
    def __init__(self,gn):
        self.gn=gn
class father (grandfather):
    def __init__(self,gn,fn):
        self.fn=fn
        grandfather .__init__(self,gn)
class son (father):
    def __init__(self,gn,fn,sn):
        self.sn=sn
        father .__init__(self,gn,fn)
    def var (self):
        print (self.gn)
        print (self.fn)
        print (self.sn)
s=son("sakthi","sasi","Thilak")
s.var()
