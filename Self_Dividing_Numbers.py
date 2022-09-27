def selfdiv(n):
    c,dc=0,0
    x=n
    while(n):
        r=n%10
        c+=1
        if(r==0):
            break
        if(x%r==0):
            dc+=1
        n=n//10
    if(c==dc):
        return 1
    else:
        return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(selfdiv(i)):
        print(i,end=" ")
        
