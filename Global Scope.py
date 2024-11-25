x=5
def var ():
    print(x)
var()
print(x)


x=5
def var ():
    x=10
    print(x)
var()
print(x)


def var ():
    global x
    x=300
var()
print(x)


x=200
def var ():
    global x
    x=300
var()
print(x)
