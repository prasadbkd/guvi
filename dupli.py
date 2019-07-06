n=int(input())
l=list(map(int,input().split()))
#print(l)
c=[]
for i in l:
    
    y=l.count(i)
    if y!=1:
        c.append(str(i))
        l.remove(i)
print(" ".join(c))
