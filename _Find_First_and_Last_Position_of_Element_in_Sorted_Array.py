n=int(input())
a=list(map(int,input().split()))
se=int(input())
c=0
for i in range(0,n):
    if(a[i]==se):
        print(i,end=' ')
        c=1
        break
while(n):
    if(a[n-1]==se):
        print(n-1)
        break
    n-=1
if(c==0):
    print("-1 -1")