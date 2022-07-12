n=int(input())
sum=0
a=list(map(int,input().split()))
b=set(a)
for i in b:
    sum+=i
print(sum)
