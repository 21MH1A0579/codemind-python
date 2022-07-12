n=int(input())
a=list(map(int,input().split()))
b=''
sum=0
c=0
for i in range(len(a)):
    if(a[i]==a.count(a[i])):
        b+=str(a[i])
c=set(b)
t=(len(c))
for j in c:
    sum+=int(j)
if (t>0):
    print('%.2f'%(sum/t))
else:
    print("-1")
