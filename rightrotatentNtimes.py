n,k = map(int,input().split())
  
list_1 = [x for x in input().split()] 
list_1 = (list_1[-k:] + list_1[:-k]) 
if len(list_1)<=2:
    list_1.reverse()
print(" ".join(list_1)) 
#prasad
