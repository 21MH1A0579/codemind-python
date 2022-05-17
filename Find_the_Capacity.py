def capacity(s,t,b):
    byte=2*s*b*t*512
    kb=byte//1024
    return kb
s,t,b=map(int,input().split())
print(capacity(s,b,t),end="KB")