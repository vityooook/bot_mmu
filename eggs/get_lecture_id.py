import time

import requests
import sqlite3

from data import config

chill = 0
count = 0
db = sqlite3.connect('/database/schedule.db')

c = db.cursor()
# date = ['2023.10.30 2023.11.05', '2023.10.16 2023.10.22']
for i in range(840, 1000):
    print(i)
    response = requests.get(f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/"
                            f"lecturer/{i}?start=2023.11.06&finish=2023.11.12&lng=1")
    if response.json() and response.status_code == 200:
        data = response.json()
        c.execute(f"INSERT INTO lecturers (lecturer_id, full_name, subject)"
                  f"VALUES ('{i}','{data[0]['lecturer_title']}', '{data[0]['discipline']}')")
        db.commit()
    if i % 50 == 0:
        time.sleep(4)


db.close()
print('finish')



# for i in itertools.permutations(alphabet, 3):
#     search_str = ''.join(i)
#     search_url = parse.quote(search_str)
#     response = requests.get(f"https://mmu2021:mmu2021@schedule.mi.university/api/search?term={search_url}&type=group")
#
#     print(response.status_code)
#
#     if response.json():
#         data = response.json()
#         for data_clear in data:
#             c.execute(f"""INSERT INTO name_of_groups (id, name, course)
#             VALUES ('{data_clear["id"]}', '{data_clear["label"]}', '{data_clear["description"]}')""")
#             db.commit()
#
#
# print(count)
# print('finish')
#
# db.close()
