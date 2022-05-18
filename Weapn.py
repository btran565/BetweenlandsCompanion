
# 2:22pm - 5.18.2022
# Class for Weapons Objects
# Note: going to set up List for Attribute scaling - [Str,Dex,Int,Fai,Arc]

class Weapn:

    # Note: self.stats in format of [Phys,Magic,Fire,Lightning,Holy]
    def __init__(self,name,wtype,attack,scaling,skill,weight,stats,flavor):
        self.name = name
        self.wtype = wtype
        self.attackType = attack
        self.scaling = self.setScaling(scaling)
        self.skill = skill
        self.weight = weight
        self.stats = stats
        self.flavorText = flavor

    def getName(self):
        return self.name

    def getType(self):
        return self.wtype

    def getAttackType(self):
        return self.attackType

    def getScaling(self):
        return self.scaling

    def getSkill(self):
        return self.skill

    def getWeight(self):
        return self.weight

    def getStats(self):
        return self.stats

    def getFlavortext(self):
        return self.flavorText

    @staticmethod
    def setScaling(scale):
        attributes = ['0','0','0','0','0']
        if 'None:' in scale:
            return attributes
        i = 0
        while i < len(scale):
            attributes[attributes.index(scale[i])] = scale[i+1]
            i += 2
        return attributes
