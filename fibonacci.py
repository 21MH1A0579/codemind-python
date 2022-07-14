n=int(input())
a=0
b=1
print(a,b,end=' ')
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=' ')
    n-=1