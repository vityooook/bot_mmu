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
    schedule_return = []
    group_id = db.execute(f"SELECT id FROM name_of_groups WHERE name='{str.upper(group_name)}'").fetchone()[0]
    data_start, data_finish = data_changing(time_data)
    response = requests.get(f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
                            f"{group_id}?start={data_start}&finish={data_finish}&lng=1")

    for add in response.json():
        data = add['date'], add['beginLesson'],add['endLesson'], add['dayOfWeekString'],add['discipline'], add['kindOfWork'], add['auditorium'], add['lecturer']
        lesson_data ={
            'data': add['date'],
            'beginLesson': add['beginLesson'],
            'endLesson': add['endLesson'],
            'dayOfWeekString': add['dayOfWeekString'],
            'discipline': add['discipline'],
            'kindOfWork': add['kindOfWork'],
            'auditorium': add['auditorium'],
            'lecturer': add['lecturer']
            }
        schedule_return.append(lesson_data)
    return schedule_return

def request_schedule(user_id, time_data):
    db.execute(f"SELECT user_id FROM users WHERE name='{str.upper(group_name)}'")

    schedule_search("экн211-2", time_data)
