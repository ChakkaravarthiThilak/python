def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y
def calc():
    a=int(input("Enter Your Choice"))
    n1=int(input("Enter Your Number"))
    n2=int(input("Enter Your Number"))
    if a==1:
        print(add(n1,n2))
    elif a==2:
        print(sub(n1,n2))
    elif a==3:
        print(multi(n1,n2))
    elif a==4:
        print(div(n1,n2))
    else:
        print("invalid")
calc()
