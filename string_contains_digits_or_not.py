n=int(input())
b="1234567890"
c=0
while(n):
    a=input()
    for i in a:
        if i in b:
            c=1
            break
        else:
            c=0
    n-=1
    if(c==0):
        print("No")
    else:
        print("Yes")