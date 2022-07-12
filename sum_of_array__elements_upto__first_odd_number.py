n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(0,len(a)):
    if a[i]%2==1:
        break
    else:
        sum+=a[i]
print(sum)
