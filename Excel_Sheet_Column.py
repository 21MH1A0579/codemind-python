n=int(input())
result='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'
while(n):
    c=chr(ord('A')+(n-1)%26)
    result=c+result
    n=(n-1)//26
print(result)