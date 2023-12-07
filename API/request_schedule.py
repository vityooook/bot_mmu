import requests
import datetime

from schemas import Lessons
from database.crud import user


def get_day_schedule(user_id: int, date):
    # получаем id группы для API
    group_id = user.get_user_group_id(user_id)
    # переводим из datetime -> str: 2023.12.07
    date_str = datetime.date.strftime(date, '%Y.%m.%d')
    # делаем запрос к API и получеем расписание на один день
    response = requests.get(
        f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
        f"{group_id}?start={date_str}&finish={date_str}&lng=1") #

    # здесь начинаешь исправлять
    all_lessons = [Lessons(**lesson) for lesson in response.json()]
    text = ''
    for lesson in all_lessons:
        text += str(lesson)
    if not text:
        text += 'Пар нет на указанную дату, кайфуем!'
    text = f"{date_str}\n" + text
    return text


def get_week_schedule(user_id: int, date):
    # get group id for API
    group_id = user.get_user_group_id(user_id) #or chat.get_group_id(user_id)
    # find first day and last day of week for API
    date_monday_unclean, date_sunday_unclean = data_changing(date)
    date_monday = datetime.date.strftime(date_monday_unclean, '%Y.%m.%d')
    date_sunday = datetime.date.strftime(date_sunday_unclean, '%Y.%m.%d')
    # requests APi and get json with lessons
    response = requests.get(
        f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
        f"{group_id}?start={date_monday}&finish={date_sunday}&lng=1")
    # тут нужно сделать расписание на неделю с красивым оформлением (на будующее)


def data_changing(time_data):
    date_week = datetime.date.weekday(time_data)
    date_monday_unclean = time_data - datetime.timedelta(date_week)
    date_sunday_unclean = date_monday_unclean + datetime.timedelta(days=6)
    return date_monday_unclean, date_sunday_unclean
