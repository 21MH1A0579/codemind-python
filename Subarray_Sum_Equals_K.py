a,b=map(int,input().split())
arr=list(map(int,input().split()))
s=c=0
for i in range(0,a):
    for j in range(i,a):
        s+=arr[j]
        if s==b:
            c+=1
        if s>b:
            break
    s=0
print(c)