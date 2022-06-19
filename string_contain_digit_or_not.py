a=input()
b="1234567890"
c=0
for i in a:
    if i in b:
        c+=1
if(c==0):
    print("Doesn't contain digit")
else:
    print("Contains",c,"digit")