def mindig(n):
    maxi=0
    while(n):
        r=n%10
        if(maxi<r):
            maxi=r
        n=n//10
    return maxi
n=int(input())
print(mindig(n))
        