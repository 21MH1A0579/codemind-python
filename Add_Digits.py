def digsum(n):
    sm=0
    while(n):
        r=n%10
        sm=sm+r
        n=n//10
    if(sm<9):
        return sm
    else:
        return digsum(sm)
n=int(input())
print(digsum(n))
    
