import math
n=int(input())
a=list(map(int,input().split()))
sum1=0
sum2=0
b=len(a)
if b%2==0:
    for i in range(0,(b//2)):
        sum1+=a[i]
    for j in range(b//2,b):
        sum2+=a[j]
else:
    for i in range(0,b//2):
        sum1+=a[i]
    for j in range(b//2,b):
        sum2+=a[j]
print(abs(sum1-sum2))
        
        
    
