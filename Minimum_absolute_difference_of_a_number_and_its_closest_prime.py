def prime(n):
    if(n==1):
        return 0
    for i in range(2,(n//2)+1):
        if (n%i==0):
            return 0
    else:
        return 1
a=int(input())
for i in range(a+1,99999999):
    if prime(i):
        x=i
        break
for j in range(a,2,-1):
    if prime(j):
        y=j
        break
if (x-a)<(a-y):
    print(x-a)
else:
    print(a-y)
        
        