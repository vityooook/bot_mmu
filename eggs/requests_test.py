import requests
from urllib import parse
import itertools
import json
import sqlite3
import time
import random

chill = 0
count = 0
db = sqlite3.connect("/Users/work/bot_mmu/bot_mmu/schedule.db")

c = db.cursor()

# alphabet = "йцукенгшзфывапролджэячсмитбю"
alphabet = "олджэячсмитбюйцукенгшзфывапр"
# alphabet = "экн"

for i in itertools.permutations(alphabet, 3):
    search_str = ''.join(i)
    # print(search_str, end="\t")
    search_url = parse.quote(search_str)
    response = requests.get(f"https://mmu2021:mmu2021@schedule.mi.university/api/search?term={search_url}&type=group")

    print(response.status_code)

    if response.json():
        data = response.json()
        for data_clear in data:
            c.execute(f"""INSERT INTO name_of_groups (id, name, course)
            VALUES ('{data_clear["id"]}', '{data_clear["label"]}', '{data_clear["description"]}')""")
            db.commit()


print(count)
print('finish')

db.close()
