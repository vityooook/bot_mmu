import requests
import sqlite3
import datetime

db = sqlite3.connect("/Users/work/bot_mmu/bot_mmu/schedule.db")


def data_changing(time_data) -> tuple[str, str]:
    data_clear = datetime.datetime.strptime(time_data, '%Y.%m.%d')
    data_week = datetime.date.weekday(data_clear)
    data_monday_unclean = data_clear - datetime.timedelta(data_week)
    data_sunday_unclean = data_monday_unclean + datetime.timedelta(days=6)
    data_monday = datetime.date.strftime(data_monday_unclean, '%Y.%m.%d')
    data_sunday = datetime.date.strftime(data_sunday_unclean, '%Y.%m.%d')
    return data_monday, data_sunday


def schedule_search(group_name, time_data):
    group_id = db.execute(f"SELECT id FROM name_of_groups WHERE name='{str.upper(group_name)}'").fetchone()[0]
    print(group_id, type(group_id))
    data_start, data_finish = data_changing(time_data)
    response = requests.get(f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
                            f"{group_id}?start={data_start}&finish={data_finish}&lng=1")
    print(response.json())
    schedule_data = response.json()
    return schedule_data


schedule_search("экн211-2", '2023.09.23')
