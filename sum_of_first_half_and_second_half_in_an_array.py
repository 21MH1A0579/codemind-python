n=int(input())
a=list(map(int,input().split()))
b=len(a)
sum1=0
sum2=0
if b%2==0:
    for i in range(len(a)):
        if(i<(len(a)//2)):
            sum1+=a[i]
        else:
            sum2+=a[i]
else:
    for i in range(len(a)):
        if(i<(len(a)//2)):
            sum1+=a[i]
        else:
            sum2+=a[i]
print(sum1)
print(sum2)