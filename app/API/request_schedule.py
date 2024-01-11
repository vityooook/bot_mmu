import datetime
from loguru import logger
from json import JSONDecodeError
from database.crud import user

import requests


@logger.catch()
async def get_week_schedule(user_id: int, date):
    # get group id for API
    group_id = await user.get_user_group_id(user_id)

    # find first day and last day of week for API
    date_monday_unclean, date_sunday_unclean = data_changing(date)
    date_monday = datetime.date.strftime(date_monday_unclean, "%Y.%m.%d")
    date_sunday = datetime.date.strftime(date_sunday_unclean, "%Y.%m.%d")

    # requests APi and get json with lessons
    response = requests.get(
        f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
        f"{group_id}?start={date_monday}&finish={date_sunday}&lng=1"
    )
    if response.status_code == 200:
        try:
            data = response.json()

            unique_discipline = []
            unique_auditorium = []
            text = []

            i = 0

            for _ in data:
                if data[i]["discipline"] not in unique_discipline:
                    unique_discipline.append(data[i]["discipline"])
                    unique_auditorium.append(data[i]["auditorium"])
                    jsondate = (
                        f"{data[i]['dayOfWeekString']} (<b>{data[i]['date']}</b>)"
                    )
                    beginLesson = (
                        f"⏱| {data[i]['beginLesson']} - {data[i]['endLesson']}"
                    )
                    discipline = f"<b>{data[i]['discipline']}</b> ({data[i]['kindOfWork'][0:3:]})"
                    auditorium = f"{data[i]['auditorium']} - {data[i]['lecturer']}"

                    text.append(jsondate)
                    text.append(beginLesson)
                    text.append(discipline)
                    text.append(auditorium)
                else:
                    if data[i]["auditorium"] not in unique_auditorium:
                        auditori = f"{data[i]['auditorium']} - {data[i]['lecturer']}"
                        text.append(auditori)
                i += 1
                text = ", \n".join(text)
            return f"""{text}"""
        except JSONDecodeError as eror:
            logger.exception(f"Ошибка декодирования JSON: {eror}")
    else:
        logger.error(f"Сайт не доступен статус кода: {response.status_code}")


@logger.catch()
async def get_day_schedule(user_id: int, date):
    group_id = await user.get_user_group_id(user_id)

    date_str = date.strftime("%Y.%m.%d")

    response = requests.get(
        f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
        f"{group_id}?start={date_str}&finish={date_str}&lng=1"
    )

    if response.status_code == 200:
        try:
            data = response.json()
            if not data:
                text = "Пар нет! кайф"
                return text
            else:
                unique_combinations = set()
                text = []
                for entry in data:
                    combination = (entry["discipline"], entry["beginLesson"])
                    if combination not in unique_combinations:
                        unique_combinations.add(combination)

                        json_date = (
                            f"{entry['dayOfWeekString']} (<b>{entry['date']}</b>)\n"
                        )
                        begin_lesson = (
                            f"\n⏱| {entry['beginLesson']} - {entry['endLesson']}"
                        )
                        discipline = f"<b>{entry['discipline']}</b> ({entry['kindOfWork'][0:3:]})"
                        auditorium = f"{entry['auditorium']} - {entry['lecturer']}"

                        text.extend([begin_lesson, discipline, auditorium])
                    else:
                        auditorium_info = f"{entry['auditorium']} - {entry['lecturer']}"
                        text.append(auditorium_info)

                text = " \n".join(text)
                return f"{json_date} {text}"
        except JSONDecodeError as error:
            logger.exception(f"Ошибка декодирования JSON {error}")
    else:
        logger.error(f"Ошибка: {response.status_code}")



@logger.catch()
def data_changing(date):
    date_week = datetime.date.weekday(date)
    date_monday_unclean = date - datetime.timedelta(date_week)
    date_sunday_unclean = date_monday_unclean + datetime.timedelta(days=6)
    return date_monday_unclean, date_sunday_unclean
