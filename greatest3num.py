#greates tnum
x,y,z=[int(x) for x in input().split()]
if x>y and x>z:
    print(x)
elif y>x and y>z:
    print(y)
else:
    print(z)
