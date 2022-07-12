n=int(input())
a=list(map(int,input().split()))
l=len(a)
if(l%2==1):
    for i in a:
        print(i,end=' ')
    print("0")
else:
    for j in a:
        print(j,end=' ')
        