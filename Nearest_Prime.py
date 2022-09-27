def prime(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
while n:
    a=int(input())
    for i in range(a,9999999):
        if prime(i):
            x=i;
            break
    for j in range(a,1,-1):
        if prime(j):
            y=j
            break
    if(x-a)<(a-y):
        print(x)
    else:
        print(y)
    n-=1
    
        