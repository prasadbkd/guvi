l,u=map(int, input().split())
li=[]
for num in range(l+1,u):
    if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                li.append(str(num))
            
            
            
            
            
print(" ".join(li))
#prasad
