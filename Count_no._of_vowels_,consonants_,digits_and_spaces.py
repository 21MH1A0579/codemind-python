n=input()
a="1234567890"
b="aeiou"
d=" "
vc=0
cc=0
dc=0
ws=0
for i in n:
    if i in a:
        dc+=1
    elif i in b:
        vc+=1
    elif i in d:
        ws+=1
    else:
        cc+=1
print("Vowels:",vc)
print("Consonants:",cc)
print("Digits:",dc)
print("White spaces:",ws)
        