def revdig(m,n):
    rev=0
    dc=0
    while(m):
        r=m%10
        dc+=1
        rev=rev*10+r
        m=m//10
        if(dc==n):
            break
    return rev
def revs(n):
    rev1=0
    while(n):
        r=n%10
        rev1=rev1*10+r
        n=n//10
    return rev1
m,n=map(int,input().split())
temp=revdig(m,n)
temp1=revs(temp)
temp2=revs(m)
temp3=revdig(temp2,n)
if(temp1-temp3<1):
    print(-(temp1-temp3))
else:
    print(temp1-temp3)
        
