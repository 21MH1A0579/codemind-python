a=int(input())
x=0
while(a):
    n=input()
    if n=="++X" or n=="X++":
        x+=1
    if n=="--X" or n=="X--":
        x-=1
    a-=1
print(x)