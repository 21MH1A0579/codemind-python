n=input()
a=0
b=0
for i in n:
    if i=='z':
        a+=1
    if i=='o':
        b+=1
if(2*a==b):
    print("Yes")
else:
    print("No")
        
    