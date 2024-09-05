import json
import random

with open("catalog_items.json", "r") as items_json:
    items = json.load(items_json)
    print(items[random.randint(0,len(items))])

input()
