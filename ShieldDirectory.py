

fileSType = open('info files\\ShieldTypes.txt','r')
fileRS = open('info files\\Shields.txt','r')

fRead = fileSType.read()
sTypes = fRead.split('\n')
print(sTypes)


fileRS.close()
fileSType.close()
