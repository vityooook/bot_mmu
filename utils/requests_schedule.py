import requests
import sqlite3
import datetime
date = datetime.

db = sqlite3.connect("/Users/work/bot_mmu/bot_mmu/schedule.db")
c = db.cursor()

info_groups = c.execute("SELECT id, name FROM name_of_groups")

for info in info_groups:
    group_id = info[0]
    group_name = info[1]

    response = requests.get(f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
                            f"{group_id}?start=2023.09.10&finish=2023.09.17&lng=1")

    for add in response.json():
        print(add['auditorium'])
        db.execute("""INSERT INTO schedule_of_groups (id, group_name, date, time_start, time_finish, dotw,
                subject, kind_of_subject, cabinet, teacher)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                  (group_id, group_name, add['date'], add['beginLesson'], add['endLesson'], add['dayOfWeekString'],
                   add['discipline'], add['kindOfWork'], add['auditorium'], add['lecturer']))
        db.commit()
db.close()

