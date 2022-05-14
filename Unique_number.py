n=int(input())
zero=0
one=0
two=0
three=0
four=0
five=0
six=0
seven=0
eight=0
nine=0
while(n):
    r=n%10
    if(r==0):
        zero+=1
    elif(r==1):
        one+=1
    elif(r==2):
        two+=1
    elif(r==3):
        three+=1
    elif(r==4):
        four+=1
    elif(r==5):
        five+=1
    elif(r==6):
        six+=1
    elif(r==7):
        seven+=1
    elif(r==8):
        eight+=1
    else:
        nine+=1
    n=n//10
if(zero<2 and one<2 and two<2 and three<2 and four<2 and five<2 and six<2 and seven<2 and eight<2 and nine<2):
    print("Unique Number")
else:
    print("Not Unique Number")