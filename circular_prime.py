def circular(n):
    temp=n
    for i in range(2,(n//2)+1):
        if(n%i==0):
            print("not prime")
            break
    else:
        rev=0
        while(n):
            r=n%10
            rev=rev*10+r
            n=n//10
        for j in range(2,(rev//2)+1):
            if(rev%j==0):
                print("prime but not a circular prime")
                break
        else:
            print("circular prime")
n=int(input())
circular(n)

            
            
            