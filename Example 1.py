def num(n):
    value=1
    while value<n:
        yield value
        value+=1
for i in num(5):
    print (i)
