import requests
import json
import item

def getAttributes():

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
def getEquipment():
    response = requests.get("https://eldenring.fanapis.com/api/weapons?limit=400")
    json_data = json.loads(response.text)
    makeDict(json_data)
    return
def makeDict(data):
    dict = {}
    for i in range(len(data['data'])):
        weapon = item.weapon(data['data'][i]['id'], data['data'][i]['name'], data['data'][i]['image'], data['data'][i]['description'], data['data'][i]['attack'], data['data'][i]['defence'], data['data'][i]['scalesWith'])
        dict[data['data'][i]['name']] = weapon
    return dict
def main():     
    #todo: input type error checking
    #user inputs character stats
    while True:
        attList = getAttributes()

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
    #while True:
    equipList = getEquipment()



main()