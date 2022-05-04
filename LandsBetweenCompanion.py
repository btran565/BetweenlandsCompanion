import requests

def attributes():

    inputs = []
    print("Welcome to the Lands Between Companion! Enter your Elden Ring character's level:")
    inputs.append(input())
    print("Enter your character's vigor:")
    inputs.append(input())
    print("Enter your character's mind:")
    inputs.append(input())
    print("Enter your character's endurance:")
    inputs.append(input())
    print("Enter your character's strength:")
    inputs.append(input())
    print("Enter your character's dexterity:")
    inputs.append(input())
    print("Enter your character's intelligence:")
    inputs.append(input())
    print("Enter your character's faith:")
    inputs.append(input())
    print("Enter your character's arcane:")
    inputs.append(input())

    return inputs
def equipment():
    #api for all equipment?????
    response = requests.get("https://eldenring.fanapis.com/api/weapons/:weapon_id")
    print (response.json())
    return

def main():     
    #todo: input type error checking
    #user inputs character stats
    while True:
        attList = attributes()

        print("Player's attributes:\n")
        print("Level: " +attList[0])
        print("Vigor: " +attList[1])
        print("Mind: " +attList[2])
        print("Endurance: " +attList[3])
        print("Strength: " +attList[4])
        print("Dexterity: "+attList[5])
        print("Intelligence: " +attList[6])
        print("Faith: " +attList[7])
        print("Arcane: " +attList[8])

        print("\nIs this correct? (yes/no)")
        answer = input()
        if answer.lower() == "yes":
            break
    while True:
        equipList = equipment()



main()