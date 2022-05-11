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
        right_hand = [right_num]
        for i in range(right_num):
            print("Right hand equipment #" + str(i + 1) + ":")
            print("Is this equipped item a Weapon or Shield?")  # need to add error checking
            item_cate = input().lower()
            item_dict = get_api(item_cate)
            if item_cate == 'weapon':
                print("Please select the equipped weapon's category:\n")
                print(
                    "Dagger, Straight Sword, Greatsword, Colossal Sword,\nThrusting Sword, Heavy Thrusting "
                    "Sword, Curved Sword, Curved Greatsword,\nKatana, Twinblade, Axe, Greataxe,\nHammer, "
                    "Flail, Great Hammer, Colossal Weapon,\nSpear, Great Spear, Halberd, Reaper,\nWhip, "
                    "Fist, Claw, Light Bow,\nBow, Greatbow, Crossbow, Ballista,\nGlintstone Staff, "
                    "Sacred Seal, Torch")
                item_cate = input()
                item_dict = algorithms.filter_category(item_dict, item_cate.lower())
                print("Choose which weapon you have equipped from the list of " + item_cate + ":\n")
                algorithms.print_dict(item_dict)
                choice = input()
                for key, value in item_dict.items():    # BROKEN. program hung up on something
                    if key.lower() == choice:
                        right_hand[i] = input()
                        print(str(right_hand[i]) + " equipped to right hand!\n")
            if item_cate == 'shield':
                print("Please select the shield's category:(small, medium, great)")
                algorithms.filter_category(item_dict, input().lower())

    # code for equipping weapons in each hand

    return


def get_api(category):  # returns dict of specified category in API   ##need to add error checking for 'category'
    json_data = {}
    for i in range(4):  # reads multiple pages of API to fill local json library
        response = requests.get("https://eldenring.fanapis.com/api/" + category + "s" + "?limit=100&page=" + "0")
        json_data.update(json.loads(response.text))
    items = algorithms.make_dict(json_data, category)
    return items





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
