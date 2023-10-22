import requests
import sqlite3
import datetime

from schemas import Lessons

db = sqlite3.connect("schedule.db")
cur = db.cursor()


def request_schedule(user_id, time_data):
    group_id = db.execute(f"SELECT name_of_groups.id FROM name_of_groups INNER JOIN users ON name_of_groups.name = "
                          f"users.user_group WHERE users.user_id='{user_id}'").fetchone()[0]
    date_monday_unclean, date_sunday_unclean = data_changing(time_data)
    date_monday = datetime.date.strftime(date_monday_unclean, '%Y.%m.%d')
    date_sunday = datetime.date.strftime(date_sunday_unclean, '%Y.%m.%d')
    response = requests.get(f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
                            f"{group_id}?start={date_monday}&finish={date_sunday}&lng=1")
    all_lessons = [Lessons(**lesson) for lesson in response.json()]
    text = ''

    for lesson in all_lessons:
        if lesson.date == time_data:
            text += str(lesson)
    if not text:
        text += 'Пар нет на указанную дату, кайфуем!'
    text = f"{datetime.date.strftime(time_data, '%Y.%m.%d')}\n" + text
    return text



def data_changing(time_data):
    date_week = datetime.date.weekday(time_data)
    date_monday_unclean = time_data - datetime.timedelta(date_week)
    date_sunday_unclean = date_monday_unclean + datetime.timedelta(days=6)
    return date_monday_unclean, date_sunday_unclean

