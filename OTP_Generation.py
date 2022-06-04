def reverse(num):
    rev=0
    while(num):
        r=num%10
        rev=rev*10+r
        num=num//10
    return rev
n=int(input())
res=reverse(n)
while(res):
    r=res%10
    if(r%2==1):
        print(r*r,end='')
    res=res//10
