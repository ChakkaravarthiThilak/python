a=("a","b","c")
b=iter(a)
print (next(b))
print (next(b))
print (next(b))


a=("a","b","c")
b=iter(a)
for i in b:
    print (i)
