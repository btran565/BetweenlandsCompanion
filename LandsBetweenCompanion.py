import requests
import json
import item


def getAttributes():
    attList = ['level', 'vigor', 'mind', 'endurance', 'strength', 'dexterity', 'intelligence', 'faith', 'arcane']
    attDict = dict(zip(attList, [None] * len(attList)))
    print("Welcome to the Lands Between Companion! Enter your Elden Ring character's level:")
    attDict[attList[0]] = input()
    print("Enter your character's vigor:")
    attDict[attList[1]] = input()
    print("Enter your character's mind:")
    attDict[attList[2]] = input()
    print("Enter your character's endurance:")
    attDict[attList[3]] = input()
    print("Enter your character's strength:")
    attDict[attList[4]] = input()
    print("Enter your character's dexterity:")
    attDict[attList[5]] = input()
    print("Enter your character's intelligence:")
    attDict[attList[6]] = input()
    print("Enter your character's faith:")
    attDict[attList[7]] = input()
    print("Enter your character's arcane:")
    attDict[attList[8]] = input()
    return attDict

def getAPI(category):
    json_data = ""
    for i in range(4):
        response = requests.get("https://eldenring.fanapis.com/api/" + category + "?limit=100&page=" + i)
        json_data += json.loads(response.text)
    items = makeDict(json_data)
    return items

def getEquipment():
    print("Enter the number of items equipped in the right hand: ")
    right = int(input())
    print("Enter the number of items equipped in the left hand: ")
    left = int(input())

    rightHand = []
    if right > 0:
        for i in range(right):
            print("Right hand equipment #" + str(i) + ": \n")
            print("What kind of equipment is this?")
    ##code for equipping weapons in each hand

    return


def makeDict(data):  # add new argument to change items in dictionary?
    dict = {}
    for i in range(len(data['data'])):
        weapon = item.Weapon(data['data'][i]['id'], data['data'][i]['name'], data['data'][i]['image'],
                             data['data'][i]['description'], data['data'][i]['attack'], data['data'][i]['defence'],
                             data['data'][i]['scalesWith'])
        dict[data['data'][i]['name']] = weapon
    return dict  # returns dictionary of item names and item objects


def main():
    # user inputs character stats
    # add input type checking later
    while True:
        attDict = getAttributes()  # creates dict of attributes
        print("Player's attributes:\n")
        for k, v in attDict.items():
            print(k.capitalize() + ': ' + v)

        print("\nIs this correct? (yes/no)")
        answer = input()
        if answer.lower() == "yes":
            break
    equipList = getEquipment()


main()
