n=int(input())
a=list(map(int,input().split()))
l=len(a)-1
k=l
m=l
if(l%2==0):
    for i in range(0,len(a)):
        if i!=(l//2) and i<l//2:
            print(a[i],a[k],end=' ')
            k=k-1
    print(a[(l//2)],0)
else:
    for j in range(0,len(a)):
        if j<(l//2)+1:
            print(a[j],a[m],end=' ')
            m=m-1
        
        
    