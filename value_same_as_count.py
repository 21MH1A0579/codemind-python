n = int(input())
a = list(map(int,input().split()))
c = 0
s=''
for i in range(len(a)):
    if a[i]==a.count(a[i]):
        s+=str(a[i])
print(len(set(s)))
