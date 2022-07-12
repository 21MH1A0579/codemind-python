n=int(input())
n,m=0,0
c=0
a=list(map(int,input().split()))
x,y=map(int,input().split())
for i in range(len(a)):
    if a[i]>x and a[i]<y or a[i]==x or a[i]==y:
        c=1
        print(a[i],end=' ')
if c==0:
    print("-1")