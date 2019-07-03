c=0
n=int(input())
s='kabali'
for i in range(0,n):
    g=input()
    if sorted(s)==sorted(g):
        c+=1
print(c)
