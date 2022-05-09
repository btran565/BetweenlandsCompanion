import requests
import json
import item
import algorithms


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

def getEquipment():     ##needs error checking for right/left ints
    print("Enter the number of items equipped in the right hand: ")
    rightNum = int(input())
    print("Enter the number of items equipped in the left hand: ")
    leftNum = int(input())

    rightHand = []
    if rightNum > 0:
        for i in range(rightNum):
            print("Right hand equipment #" + str(i+1) + ":")
            print("Is this equipped item a Weapon or Shield?\n")
            itemCate = input().lower()
            itemDict = getAPI(itemCate)
            if itemCate == 'weapon':
                print("Please select a weapon category:")
                print("(Daggers\nStraight Swords\nGreatswords\nColossal Swords\nThrusting Swords\nHeavy Thrusting Swords\nCurved Swords\nCurved Greatswords\nKatanas\nTwinblades\nAxes\nGreataxes\nHammers\nFlails\nGreat Hammers\nColossal Weapons\nSpears\nGreat Spears\nHalberds\nReapers\nWhips\nFists\nClaws\nLight Bows\nBows\nGreatbows\nCrossbows\nBallistae\nGlintstone STaffs\nSacred Seals\nTorches)")
                algorithms.getCategoryList(itemDict, input().lower())
            if itemCate == 'shield':
                print("Please select a shield category(small, medium, great)")
                algorithms.getCategoryList(itemDict, input().lower())

    ##code for equipping weapons in each hand

    return

def getAPI(category):    #returns dict of specified category in API   ##need to add error checking for 'category'
    json_data = {}
    for i in range(4):      #reads multiple pages of API to fill local json library
        response = requests.get("https://eldenring.fanapis.com/api/" + category + "s" + "?limit=100&page=" + "0")
        json_data.update(json.loads(response.text))
    items = makeDict(json_data, category)
    return items

def makeDict(data, category):  #takes json data and category and makes dict ## add more conditionals to make dicts of other categories
    dict = {}
    if (category == "weapon"):
        for i in range(len(data['data'])):
            weapon = item.Weapon(data['data'][i]['id'], data['data'][i]['name'], data['data'][i]['image'],
                                 data['data'][i]['description'], data['data'][i]['category'], data['data'][i]['weight'], data['data'][i]['attack'], data['data'][i]['defence'], data['data'][i]['requiredAttributes'],
                                 data['data'][i]['scalesWith'])
            dict[data['data'][i]['name']] = weapon
    if (category == "shield"):
        for i in range(len(data['data'])):
            shield = item.Weapon(data['data'][i]['id'], data['data'][i]['name'], data['data'][i]['image'],
                                 data['data'][i]['description'], data['data'][i]['category'], data['data'][i]['weight'], data['data'][i]['attack'], data['data'][i]['defence'], data['data'][i]['requiredAttributes'],
                                 data['data'][i]['scalesWith'])
            dict[data['data'][i]['name']] = shield
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
