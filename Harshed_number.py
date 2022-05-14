def harshed(n):
    temp=n
    sm=0
    while(n):
        r=n%10
        sm+=r
        n=n//10
    if(temp%sm==0):
        return True
    else:
        return False
n=int(input())
print(harshed(n))
    
        