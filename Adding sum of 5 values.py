def var(n):
    if n>0:
        result=n+var(n-1)
        print(result)
    else:
        result=0
    return result
var(6)
