import json
import item


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

def filter_category(item_dict, category):
    new_dict = dict()
    for (key, value) in item_dict.items():
        if value.category == category:
            new_dict[key] = value
    return new_dict

def print_dict(dict):
    for i in range(len(dict)):
        # print(dict[])