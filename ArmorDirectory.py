# Armor Directory for project

fileAType = open('info files\\ArmorTypes.txt','r')
fileRA = open('info files\\Armors.txt','r')

fRead = fileAType.read()
aTypes = fRead.split('\n')
print(aTypes)

fRead = fileRA.read()
aList = [x.split(',') for x in fRead.split('\n')]

for i in aList:
    i.pop()
    print(i[1], " : ", (i[1] in aTypes))

aOList = [[],[],[],[]]

for i in aList:
    aOList[aTypes.index(i[1])].append(i[0])

for i in range(4):
    print(aTypes[i],": ",len(aOList[i])," : ",aOList[i])


fileRA.close()
fileAType.close()

