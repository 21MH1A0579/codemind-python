def happy(n):
    sm=0
    while(n):
        r=n%10
        sm+=(r**2)
        n=n//10
    if(sm<9):
        if(sm==1 or sm==7):
            return True
        else:
            return False
    else:
        return happy(sm)
        
n=int(input())
print(happy(n))
            
        
        