n=int(input())
a=list(map(int,input().split()))
sum1=0
sum=0
for i in range(0,n):
    if(i%2==1):
        sum+=a[i]
    else:
        sum1+=a[i]
if(sum-sum1==0):
    print("YES")
else:
    print("NO")