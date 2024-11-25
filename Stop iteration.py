class num:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=10:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
x=num()
b=iter(x)
for i in x:
    print(i)
