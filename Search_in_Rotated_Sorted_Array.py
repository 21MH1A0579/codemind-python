n=int(input())
a=list(map(int,input().split()))
se=int(input())
c=0
for i in range(0,n):
    if(a[i]==se):
        print(i)
        c=1
if(c==0):
    print("-1")