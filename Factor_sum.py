def factors(n):
    sum=1
    for j in range(2,n+1):
        if n%j==0:
            sum+=j
    return sum
            
s=input()
s=s.split(",")
res=[]
for i in s:
    b= factors(int(i))
    if str(b) in s:
        res.append(int(i))
if len(res)==0:
    print("-1")
else:
    print(*sorted(res))