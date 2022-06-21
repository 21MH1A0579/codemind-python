n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    for j in range(0,n):
        if(a[i]==a[j] and i!=j):
            c=1
    if(c==1):
        print(a[i])
        break