def divisors(n):
    c=0
    np=0
    for i in range(2,n+1):
        if(n%i==0):
            for j in range(2,(i//2)+1):
                if(i%j==0):
                    c+=1
                    break
    return c
n=int(input())
print(divisors(n)+1)
            