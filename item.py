class Weapon:       #used for both Weapons and Shields
    def __init__(self, id, name, image, description, category, weight, attack, defence, required_attributes, scales_with):
        self.id = id
        self.name = name
        self.image = image
        self.description = description
        self.category = category
        self.weight = weight
        self.attack = attack
        self.defence = defence
        self.requiredAttributes = required_attributes
        self.scalesWith = scales_with


