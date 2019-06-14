n=input()
y=[]
for i in n:
    y.append(65+(ord(i)-65+3)%26)
for i in range(len(y)):    
    y[i]=chr(y[i])
print("".join(y))
#prasad
