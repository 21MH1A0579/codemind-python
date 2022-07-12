n=int(input())
a=list(map(int,input().split()))
b=set(a)
s=''
for i in range(len(a)):
    if a[i]==a.count(a[i]):
        s+=str(a[i])
k=set(s)
if(k):
    print(min(k),max(k))
else:
    print("-1")