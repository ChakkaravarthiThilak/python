for i in range(5):
    for j in range(4,i,-1):
        print(" ",end='')
    for k in range(i+1):
        print('*',end= '')
    print()
for i in range(1,5):
    for j in range(i):
        print(" ",end='')
    for k in range(4,i-1,-1):
        print('*',end='')
    print()
