n=int(input())
a=list(map(int,input().split()))
mx=0
c=0
for i in range(0,n):
    c=0
    for j in range(0,n):
        if(a[i]==a[j]):
            c+=1
    if(c>mx):
        mx=c
        z=a[i]
print(z)
