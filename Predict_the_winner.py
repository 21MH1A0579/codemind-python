n=int(input())
sum=0
sum1=0
a=list(map(int,input().split()))
for i in range(0,n):
    if(i%2==0):
        sum+=a[i]
    else:
        sum1+=a[i]
res=sum-sum1
if(res<0):
    res=-1*res
if(res%4==0):
    print("X")
else:
    print("Y")
    