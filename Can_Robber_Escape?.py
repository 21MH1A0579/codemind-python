a=int(input())
sum=0
n=list(map(int, input().split()))
for i in range(0,a):
    if n[i]%2==1:
        sum+=1
if(sum>2):
    print("NO")
else:
    print("YES")


    