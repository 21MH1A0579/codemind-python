def autom(n):
    dc=0
    temp1=n
    while(n):
        dc+=1
        n=n//10
    sq=temp1**2
    sdc=0
    rev=0
    while(sq):
        r=sq%10
        sdc+=1
        rev=rev*10+r
        if(sdc==dc):
            break
        sq=sq//10
    return rev
def revs(n):
    rev1=0
    while(n):
        r2=n%10
        rev1=rev1*10+r2
        n=n//10
    return rev1
n=int(input())
temp=autom(n)
if(revs(temp)==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

    
        
