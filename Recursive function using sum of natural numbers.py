def var(n):
    if n<=1:
        return n
    else:
        result=n+var(n-1)
        return result
n=int(input("Enter your number"))
print("The sum is",var(n))
