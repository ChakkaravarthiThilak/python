M1=int(input("Mark 1"))
M2=int(input("Mark 2"))
M3=int(input("Mark 3"))
a=M1*M2*M3
b=a/3
if a>90:
    print("Grade A")
elif b>=80 and b<90:
    print("Grade B")
elif b>=70 and b<80:
    print("Grade C")
elif b>=60 and b<70:
    print("Grade D")
elif b<60:
    print("Fail")
    
