def divsum(x):
    sm=0
    for i in range(1,(n//2)+1):
        if(x%i==0):
            sm+=i
    return sm
m=int(input())
n=int(input())
temp=divsum(m)
temp1=divsum(n)
if(temp==n and temp1==m):
    print("Amicable")
else:
    print("Not Amicable")
