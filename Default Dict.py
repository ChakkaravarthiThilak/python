from collections import defaultdict
d=defaultdict(int)
l=[1,2,3,4,2,4,1,2]
for i in l:
    d[i]+=1
print (d)
