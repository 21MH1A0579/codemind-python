n=int(input())
a=list(map(int,input().split()))
for i in range(0,n):
    prd=1
    for j in range(0,n):
        if(i!=j):
            prd=prd*a[j]
    print(prd,end=" ")
            