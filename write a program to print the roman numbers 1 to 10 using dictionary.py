a={1:'I',
     2:'II',
     3:'III',
     4:'IV',
     5:'V',
     6:'VI',
     7:'VII',
     8:'VIII',
     9:'IX',
     10:'X'
   }
b=int(input("number"))
if b not in a:
    print("invalid")
else:
    print("numeric version of ", b,"is",a[b])
