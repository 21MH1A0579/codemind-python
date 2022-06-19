a=input()
b="1234567890"
sum=0
n=len(a)
for i in range(0,n):
    if a[i] in b:
        sum+=int(a[i])
print(sum)