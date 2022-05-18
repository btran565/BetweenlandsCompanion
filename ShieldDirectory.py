

fileSType = open('info files\\ShieldTypes.txt','r')
fileRS = open('info files\\Shields.txt','r')

fRead = fileSType.read()
sTypes = fRead.split('\n')
print(sTypes)

fRead = fileRS.read()
sList = [x.split(',') for x in fRead.split('\n')]

sOList = [[],[],[]]

for i in sList:
    i.pop()
    sOList[sTypes.index(i[1])].append(i[0])

for i in range(3):
    print(sTypes[i],": ",len(sOList[i])," : ",sOList[i])


fileRS.close()
fileSType.close()
