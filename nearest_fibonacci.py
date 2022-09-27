n=int(input())
a=0
b=1
c=1
while(c<=n):
    a=b
    b=c
    c=a+b
if(n-b)<(c-n):
    print(b)
elif(n-b)>(c-n):
    print(c)
else:
    print(b,c)
    
