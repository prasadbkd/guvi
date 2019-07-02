n,k = map(int,input().split())
  
list_1 = [x for x in input().split()] 
list_1 = (list_1[-k:] + list_1[:-k]) 
print(" ".join(list_1)) 
#prasad
