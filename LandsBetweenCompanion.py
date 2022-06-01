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
    get_api('weapons')
    return


def get_api(category):  # returns dict of specified category in API   ##need to add error checking for 'category'
    # json_data = {}
    for i in range(4):  # reads multiple pages of API to fill local json library
        json_data = requests.get("https://eldenring.fanapis.com/api/" + str(category) + "?limit=100&page=" + "0").json()
        print(json_data)
        # json_data.update(json.loads(response))
        with open('test.json', 'w') as json_file:
            json.dump(json_data, json_file)


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


if __name__ == "__main__":
    main()
