# Doin the hashtable sha blam
import random

x = random.randrange(0,10)

print(x)


def hashindex(elem):
    total = 0
    for i in elem:
        total += ord(i)
    return total % 100

sample = "Short Sword"

print(hashindex(sample))

# Beyond singular functions, need to implement a proper class structure for data
# 1:47am - 5.10.2022: Plans for making a hashtable class,
# Level 1: General weapon classes, i.e. Offensive weapons, Bows, Shields
# Level 2: Sub Classes for weapons, i.e. Greatswords, Colossal Swords, etc
# Level 3: Actual list for weapons, will consider list vs. tree argument
# Personal Note: the PEP8 reminders in the compiler are very annoying, will look into removing them

# 1:55 pm - 5.10.2022: Intentions for class structure,
# May require user input for determining section required, then subsequent hashing for each individual weapon
# Might need to make changes to incorporate the differences in weapon viability
# Best storage practices might be to organize by capability/ power level as opposed to spelling
# hash function will need adjustment






