import requests
import json
import item
import algorithms


def get_attributes():
    attList = ['level', 'vigor', 'mind', 'endurance', 'strength', 'dexterity', 'intelligence', 'faith', 'arcane']
    attDict = dict(zip(attList, [None] * len(attList)))  # creates dict with attributes as keys and None's as values
    print("Welcome to the Lands Between Companion!\n")
    for i in range(len(attList)):
        print("Enter your character's " + attList[i] + ":")
        attDict[attList[i]] = input()
    return attDict


def get_equipment():  # needs error checking for right/left ints
    print("Enter the number of items equipped in the right hand: ")
    rightNum = int(input())
    print("Enter the number of items equipped in the left hand: ")
    leftNum = int(input())

    rightHand = []
    if rightNum > 0:
        for i in range(rightNum):
            print("Right hand equipment #" + str(i + 1) + ":")
            print("Is this equipped item a Weapon or Shield?\n")
            itemCate = input().lower()
            itemDict = get_api(itemCate)
            if itemCate == 'weapon':
                print("Please select the weapon's category:")
                print(
                    "Daggers, Straight Swords, Greatswords, Colossal Swords,\nThrusting Swords, Heavy Thrusting "
                    "Swords, Curved Swords, Curved Greatswords,\nKatanas, Twinblades, Axes, Greataxes,\nHammers, "
                    "Flails, Great Hammers, Colossal Weapons,\nSpears, Great Spears, Halberds, Reapers,\nWhips, "
                    "Fists, Claws, Light Bows,\nBows, Greatbows, Crossbows, Ballistae,\nGlintstone Staffs, "
                    "Sacred Seals, Torches")
                algorithms.getCategoryList(itemDict, input().lower())
            if itemCate == 'shield':
                print("Please select the shield's category:(small, medium, great)")
                algorithms.getCategoryList(itemDict, input().lower())

    ##code for equipping weapons in each hand

    return


def get_api(category):  # returns dict of specified category in API   ##need to add error checking for 'category'
    json_data = {}
    for i in range(4):  # reads multiple pages of API to fill local json library
        response = requests.get("https://eldenring.fanapis.com/api/" + category + "s" + "?limit=100&page=" + "0")
        json_data.update(json.loads(response.text))
    items = make_dict(json_data, category)
    return items


def make_dict(data, category):
    # takes json data and category and makes dict
    # add more conditionals to make dicts of other categories
    dict = {}
    if (category == "weapon"):
        for i in range(len(data['data'])):
            weapon = item.Weapon(data['data'][i]['id'], data['data'][i]['name'], data['data'][i]['image'],
                                 data['data'][i]['description'], data['data'][i]['category'], data['data'][i]['weight'],
                                 data['data'][i]['attack'], data['data'][i]['defence'],
                                 data['data'][i]['requiredAttributes'],
                                 data['data'][i]['scalesWith'])
            dict[data['data'][i]['name']] = weapon
    if (category == "shield"):
        for i in range(len(data['data'])):
            shield = item.Weapon(data['data'][i]['id'], data['data'][i]['name'], data['data'][i]['image'],
                                 data['data'][i]['description'], data['data'][i]['category'], data['data'][i]['weight'],
                                 data['data'][i]['attack'], data['data'][i]['defence'],
                                 data['data'][i]['requiredAttributes'],
                                 data['data'][i]['scalesWith'])
            dict[data['data'][i]['name']] = shield
    return dict  # returns dictionary of item names and item objects


def main():
    # user inputs character stats
    # add input type checking later
    while True:
        att_dict = get_attributes()  # creates dict of attributes
        print("Player's attributes:\n")
        for k, v in att_dict.items():
            print(k.capitalize() + ': ' + v)

        print("\nIs this correct? (yes/no)")
        answer = input()
        if answer.lower() == "yes":
            break
    equip_list = get_equipment()


main()
