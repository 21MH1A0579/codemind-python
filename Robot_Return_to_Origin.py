n=input()
lc=0
rc=0
uc=0
dc=0
for i in n:
    if(i=="U"):
        uc+=1
    elif(i=="D"):
        dc+=1
    elif(i=="L"):
        lc+=1
    elif(i=="R"):
        rc+=1
if((lc==rc==1) or (uc==dc==1)):
    print("True")
else:
    print("False")