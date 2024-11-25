num=int(input(" "))
sum=0
temp=num
while temp>0:
    a=temp%10
    sum+=a*a*a*a
    temp=temp//10
if sum==num:
    print("Armstrong")
else:
    print("Not")
    
