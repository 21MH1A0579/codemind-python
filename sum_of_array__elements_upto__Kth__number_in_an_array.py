n=int(input())
a=list(map(int,input().split()))
x=int(input())
sum=0
for i in range(len(a)):
    if a[i]==x:
        k=i
for i in range(k+1):
    sum+=a[i]
print(sum)
    

