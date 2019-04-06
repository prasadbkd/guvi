n=int(input())
t=1
if n<=1000:
    
    for i in range(2,13):
        if n%i==0:
            t+=1
    
    if t==1:
        print('yes')
    else:
        print('no')
else:
        print('no')
 #prasad
