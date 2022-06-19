a=input()
b=int(input())
c=len(a)
d=b//c
ct=0
for i in a:
    if i=="a":
        ct+=1
e=d*ct
f=b%c
for j in range(0,f):
    if(a[j]=="a"):
        e+=1
print(e)
    
        