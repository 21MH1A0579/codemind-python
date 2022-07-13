n=int(input())
s=''
c=0
a=list(map(int,input().split()))
k=int(input())
for i in range(n):
    if a.count(a[i])==k:
        c=1
        s+=str(a[i])
if c==0:
    print("-1")
else:
    for j in sorted(set(s)):
        print(j,end=' ')