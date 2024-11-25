import math
a=int(input("number of persons"))
b=int(input("number of hotdog packets"))
c=a*b
d=math.ceil(c/10)
print(d)
e=math.ceil(c/8)
print(e)
f=d*10-c
print(f)
g=e*8-c
print(g)
