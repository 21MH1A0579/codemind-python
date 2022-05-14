def hcf(a,b):
    n=b
    while(n):
        if(a%n==0 and b%n==0):
            return n
        n-=1
m,n=map(int,input().split())
print(hcf(m,n))