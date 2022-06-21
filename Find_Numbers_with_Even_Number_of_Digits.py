def digit(n):
    c=0
    while(n):
        c+=1;
        n=n//10
    if(c%2==0):
        return True
    else:
        return False
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    
    if(digit(a[i])):
        c+=1
print(c)