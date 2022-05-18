# 11:05pm - 5.17.2022: All previous comments and code has been deleted because it was
# useless trash.
# New plan of action
# Note: I absolutely hate the PEP8 reminders, half require me to unlearn proper protocol in
# every other language

fileWType = open('info files\\WeaponTypes.txt','r')

fRead = fileWType.read()
wTypes = fRead.split('\n')

print(wTypes)

fileWType.close()
