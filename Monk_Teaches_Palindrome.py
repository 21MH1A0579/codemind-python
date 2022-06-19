a=int(input())
while(a):
    n=input()
    x=len(n)
    if n==n[::-1]:
        print("YES",end=' ')
        if(x%2==0):
            print("EVEN")
        else:
            print("ODD")
    else:
        print("NO")
    a-=1