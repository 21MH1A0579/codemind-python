def primecount(n):
    pc=0
    for j in range(1,n+1):
        if(n%j==0):
            pc+=1
    if(pc==2):
        return n
        return True
    else:
        return False
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if(primecount(i)):
        print(primecount(i))
        
        
            
