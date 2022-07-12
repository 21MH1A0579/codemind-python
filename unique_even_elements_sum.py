n=int(input())
sum=0
a=list(map(int,input().split()))
b=set(a)
for i in b:
    if i%2==0:
        sum+=i
print(sum)