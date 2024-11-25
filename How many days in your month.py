a=(input("Enter your M0nth"))
b=[m.strip() for m in a.split(',')]
for i in b:
    if i=="febuary":
        print("28/29 days")
    elif i in("January","March","May","July","September","November"):
        print(i,"has 31 Days")
    elif i in("April","June","Auguest","October","December"):
        print(i,"has 30 Days")
    else:
        print(i,"invalid")
