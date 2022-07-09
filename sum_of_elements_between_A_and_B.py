n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
sum=0
for i in range(len(arr)):
    if(arr[i]>a and arr[i]<b or (arr[i]==a or arr[i]==b)):
        sum+=arr[i]
print(sum)
