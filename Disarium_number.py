def disarium(n):
    c=0
    temp=n
    temp1=n
    while(n):
        r=n/10
        c+=1
        n=n//10
    sm=0
    while(temp and c>0):
        r=temp%10
        sm+=(r**c)
        temp=temp//10
        c-=1
    if(temp1==sm):
        return True
    else:
        return False
n=int(input())
print(disarium(n))
    
        
    