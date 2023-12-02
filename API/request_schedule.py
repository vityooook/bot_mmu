import datetime

import requests

from database.crud import group, chat
from pydantic import BaseModel, field_validator, ValidationError

class Lessons(BaseModel):
    date: datetime.date  # Дата!
    dayOfWeekString: str  # День недели
    beginLesson: str  # Начало пары
    endLesson: str  # Конец пары
    discipline: str  # Дисциплина / Пара
    kindOfWork: str  # Какие занятия
    auditorium: str  # Аудитория
    lecturer: str  # Преподаватель

    @field_validator("date", mode="before")
    @classmethod
    def date_validator(cls, value):
        try:
            year, month, day = map(int, value.split("."))
            return datetime.date(year, month, day)

        except ValidationError:
            raise ValidationError("Wrong data format")
        
    def __str__(self):
        my_var = ''
        for i in self.auditorium:
            my_var += i
        


        return f"""Иностранный язк {my_var}"""


def request_schedule(user_id, time_data):
    # get group id for API
    group_id = group.get_group_id(user_id) or chat.get_group_id(user_id)
    # find first day and last day of week for API
    date_monday_unclean, date_sunday_unclean = data_changing(time_data)
    date_monday = datetime.date.strftime(date_monday_unclean, '%Y.%m.%d')
    date_sunday = datetime.date.strftime(date_sunday_unclean, '%Y.%m.%d')
    # requests APi and get json with lessons
    response = requests.get(
        f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
        f"{group_id}?start={date_monday}&finish={date_sunday}&lng=1")
    all_lessons = [Lessons(**lesson) for lesson in response.json()]
    text = ''
    duplicate = []

    # process the data and turn into str
    for lesson in all_lessons: # Цикл for перебираем полученное из JSON файла
        for i in lesson.auditorium:
            print(i)
    if lesson.date == time_data:  # Сравниваем полученную дату из JSON с датой на данный момент time_data
        pass
    if not text:
        text += 'Пар нет на указанную дату, кайфуем!'
    text = f"{datetime.date.strftime(time_data, '%Y.%m.%d')}\n"
    return text


def data_changing(time_data):
    date_week = datetime.date.weekday(time_data)
    date_monday_unclean = time_data - datetime.timedelta(date_week)
    date_sunday_unclean = date_monday_unclean + datetime.timedelta(days=6)
    return date_monday_unclean, date_sunday_unclean
