numList='7316717653133'
posStart=0
posEnd=13
proMax=0

while posEnd<=len(numList):
    pro=1
    for i in numList[posStart:posEnd]:
        pro*=int(i)
    if pro>proMax:
        proMax= pro
    posStart+=1
    posEnd+=1

print(proMax)