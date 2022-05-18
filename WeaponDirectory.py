# 11:05pm - 5.17.2022: All previous comments and code has been deleted because it was
# useless trash.
# New plan of action
# Note: I absolutely hate the PEP8 reminders, half require me to unlearn proper protocol in
# every other language

# from Weapn import Weapn


fileWType = open('info files\\WeaponTypes.txt','r')
fileRW = open('info files\\Weapons.txt','r')

fRead = fileWType.read()
wTypes = fRead.split('\n')
print(wTypes)

fRead = fileRW.read()

wList = [x.split(',') for x in fRead.split('\n')]
wList.pop()

count = 0

for i in wList:
    i.pop()

wOList = [[] for i in range(len(wTypes))]

for i in wList:
    wOList[wTypes.index(i[1])].append(i[0])

for i in range(len(wOList)):
    print(wTypes[i]," : ",len(wOList[i])," : ",wOList[i])

fileRW.close()
fileWType.close()
