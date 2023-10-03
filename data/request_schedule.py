import requests
import sqlite3
import datetime

from schemas import Lessons

db = sqlite3.connect("/Users/work/bot_mmu/bot_mmu/schedule.db")


def request_schedule(user_id, time_data):
    group_name = db.execute(f"SELECT user_group FROM users WHERE user_id='{user_id}'").fetchone()[0]
    return schedule_search(group_name, time_data)


def schedule_search(group_name, time_data):
    group_id = db.execute(f"SELECT id FROM name_of_groups WHERE name='{str.upper(group_name)}'").fetchone()[0]
    data_start, data_finish = data_changing(time_data)
    response = requests.get(f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
                            f"{group_id}?start={data_start}&finish={data_finish}&lng=1")

    all_lessons = [Lessons(**lesson) for lesson in response.json()]
    text = ''
    for lesson in all_lessons:
        if lesson.date == time_data:
            text += f"""
{lesson.beginLesson} - {lesson.endLesson}
<b>{lesson.discipline}</b>({lesson.kindOfWork})
{lesson.auditorium} {lesson.lecturer}
"""
    if text == '':
        text = 'пар нету, кайфуем'
    return text


def data_changing(time_data) -> tuple[str, str]:
    data_clear = datetime.datetime.strptime(time_data, '%Y.%m.%d')
    data_week = datetime.date.weekday(data_clear)
    data_monday_unclean = data_clear - datetime.timedelta(data_week)
    data_sunday_unclean = data_monday_unclean + datetime.timedelta(days=6)
    data_monday = datetime.date.strftime(data_monday_unclean, '%Y.%m.%d')
    data_sunday = datetime.date.strftime(data_sunday_unclean, '%Y.%m.%d')
    return data_monday, data_sunday



