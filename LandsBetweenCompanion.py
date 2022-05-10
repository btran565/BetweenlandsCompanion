import requests
import json
import item
import algorithms


def get_attributes():
    att_list = ['level', 'vigor', 'mind', 'endurance', 'strength', 'dexterity', 'intelligence', 'faith', 'arcane']
    att_dict = dict(zip(att_list, [None] * len(att_list)))  # creates dict with attribute keys and None values
    print("Welcome to the Lands Between Companion!\n")
    for i in range(len(att_list)):
        while True:
            att_dict[att_list[i]] = input("Enter your character's " + att_list[i] + ": ")
            try:
                user_input = int(att_dict[att_list[i]])
                if att_list[i] == 'level':
                    if user_input <= 0 or user_input > 713:
                        print('ERROR: Level must be between 0-713.')
                        continue
                    else:
                        break
            except ValueError:
                print('ERROR: Valid number required.')
                continue
            if 0 <= user_input <= 99:
                break
            else:
                print('ERROR: Attribute must be between 0-100.')
    return att_dict


def get_equipment():  # needs error checking for right/left ints
    print("Enter the number of items equipped in the right hand: ")
    right_num = int(input())
    print("Enter the number of items equipped in the left hand: ")
    left_num = int(input())

    both_hands = []
    if right_num > 0:
        for i in range(right_num):
            print("Right hand equipment #" + str(i + 1) + ":")
            print("Is this equipped item a Weapon or Shield?\n")    # need to add error checking
            item_cate = input().lower()
            item_dict = get_api(item_cate)
            if item_cate == 'weapon':
                print("Please select the weapon's category:")
                print(
                    "Daggers, Straight Swords, Greatswords, Colossal Swords,\nThrusting Swords, Heavy Thrusting "
                    "Swords, Curved Swords, Curved Greatswords,\nKatanas, Twinblades, Axes, Greataxes,\nHammers, "
                    "Flails, Great Hammers, Colossal Weapons,\nSpears, Great Spears, Halberds, Reapers,\nWhips, "
                    "Fists, Claws, Light Bows,\nBows, Greatbows, Crossbows, Ballistae,\nGlintstone Staffs, "
                    "Sacred Seals, Torches")
                algorithms.get_category_list(item_dict, input().lower())
            if item_cate == 'shield':
                print("Please select the shield's category:(small, medium, great)")
                algorithms.get_category_list(item_dict, input().lower())

    # code for equipping weapons in each hand

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
    new_dict = {}
    if category == "weapon":
        for i in range(len(data['data'])):
            weapon = item.Weapon(data['data'][i]['id'], data['data'][i]['name'], data['data'][i]['image'],
                                 data['data'][i]['description'], data['data'][i]['category'], data['data'][i]['weight'],
                                 data['data'][i]['attack'], data['data'][i]['defence'],
                                 data['data'][i]['requiredAttributes'],
                                 data['data'][i]['scalesWith'])
            new_dict[data['data'][i]['name']] = weapon
    if category == "shield":
        for i in range(len(data['data'])):
            shield = item.Weapon(data['data'][i]['id'], data['data'][i]['name'], data['data'][i]['image'],
                                 data['data'][i]['description'], data['data'][i]['category'], data['data'][i]['weight'],
                                 data['data'][i]['attack'], data['data'][i]['defence'],
                                 data['data'][i]['requiredAttributes'],
                                 data['data'][i]['scalesWith'])
            new_dict[data['data'][i]['name']] = shield
    return new_dict  # returns dictionary of item names and item objects


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
