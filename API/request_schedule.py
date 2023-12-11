import datetime

from json import JSONDecodeError
from shlex import join
from database.crud import user

import requests


def get_week_schedule(user_id: int, date):
    # get group id for API
    group_id = user.get_user_group_id(user_id)

    # find first day and last day of week for API
    date_monday_unclean, date_sunday_unclean = data_changing(date)
    date_monday = datetime.date.strftime(date_monday_unclean, '%Y.%m.%d')
    date_sunday = datetime.date.strftime(date_sunday_unclean, '%Y.%m.%d')

    # requests APi and get json with lessons
    response = requests.get(
        f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
        f"{group_id}?start={date_monday}&finish={date_sunday}&lng=1")
    if response.status_code == 200:
        try:
            data = response.json()

            unique_discipline = []
            unique_auditorium = []
            text = []

            i = 0

            for _ in data:
                if data[i]['discipline'] not in unique_discipline:

                    unique_discipline.append(data[i]['discipline'])
                    unique_auditorium.append(data[i]['auditorium'])
                    # Ничего умнее я не придумал)
                    # Суббота (09.12.2023)
                    jsondate = f"{data[i]['dayOfWeekString']} (<b>{data[i]['date']}</b>)"
                    # ⏱️ | 10:30 - 11:50
                    beginLesson = f"⏱| {data[i]['beginLesson']} - {data[i]['endLesson']}"
                    # Методы принятия управленческих решений (Лек)
                    discipline = f"<b>{data[i]['discipline']}</b> ({data[i]['kindOfWork'][0:3:]})"
                    # 219(п) - Ф.И.О
                    auditorium = f"\n{data[i]['auditorium']} - {data[i]['lecturer']}"

                    text.append(jsondate)
                    text.append(beginLesson)
                    text.append(discipline)
                    text.append(auditorium)

                    print(unique_discipline[-1])
                    print(unique_auditorium[-1])
                else:
                    if data[i]['auditorium'] not in unique_auditorium:

                        # ⏱️ | 10:30 - 11:50
                        beginLesson = f"⏱| {data[i]['beginLesson']} - {data[i]['endLesson']}"
                        # Методы принятия управленческих решений (Лек)
                        discipline = f"<b>{data[i]['discipline']}</b> ({data[i]['kindOfWork'][0:3:]})"
                        # добавить препод
                        auditorium = f"{data[i]['auditorium']} - {data[i]['lecturer']}"

                        text.append(beginLesson)
                        text.append(discipline)
                        text.append(auditorium)
                i += 1
                text = ', \n'.join(text)
            return f"""{text}"""
        except JSONDecodeError:
            print('Ответ не удалось обработать')
    else:
        print("Сайт не доступен")


def get_day_schedule(user_id: int, date):
    # get group id for API
    group_id = user.get_user_group_id(user_id)

    # find first day and last day of week for API
    date_str = datetime.date.strftime(date, '%Y.%m.%d')

    # requests APi and get json with lessons
    response = requests.get(
        f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
        f"{group_id}?start={date_str}&finish={date_str}&lng=1")
    # Проверка статуса ответа от сайта
    if response.status_code == 200:
        # Блок try так же ловим ошибки
        try:
            # Применяем содержимое JSON в data
            data = response.json()
            if not data:
                text = "Пар нет! кайф"
            else:
                # Передаем data в функцию compare_discipline
                # Обычнный список сюда будут записываться уникальные str
                unique_discipline = []
                unique_begin = []
                text = []
                # Переменная счетчика
                i = 0
                # Цикл for для перебора получаемых данных из JSON
                for _ in data:
                    # Проверка на уникальность данных из data[i]['discipline'], если str уникальная то идем дальше
                    if data[i]['discipline'] not in unique_discipline and data[i]['beginLesson'] not in unique_begin:

                        # Добавляем в конец списка уникальный str из data[i]['discipline'] в список unique_discipline
                        unique_discipline.append(data[i]['discipline'])
                        unique_begin.append(data[i]['auditorium'])
                        # Ничего умнее я не придумал)
                        # Суббота (09.12.2023)
                        jsondate = f"{data[i]['dayOfWeekString']} (<b>{data[i]['date']}</b>)\n"
                        # ⏱️ | 10:30 - 11:50
                        beginLesson = f"\n⏱| {data[i]['beginLesson']} - {data[i]['endLesson']}"
                        # Методы принятия управленческих решений (Лек)
                        discipline = f"<b>{data[i]['discipline']}</b> ({data[i]['kindOfWork'][0:3:]})"
                        # 219(п) - Ф.И.О
                        auditorium = f"{data[i]['auditorium']} - {data[i]['lecturer']}\n"

                        
                        text.append(beginLesson)
                        text.append(discipline)
                        text.append(auditorium)
                    # Выводим на принт последний элемент из списка

                        print(unique_discipline[-1])
                        print(unique_begin[-1])
                    # Выводим на принт data[i]['auditorium'] str аудиторию
                    # Блок else если у нас при проверке получен не уникальный data[i]['discipline']
                    else:
                    
                        # print(data[i]['discipline']) тут я закоментил бред
                        # Выводим на принт data[i]['auditorium'] будет выводиться каждый раз когда у нас не уникальный str в data[i]['discipline']

                        # ⏱️ | 10:30 - 11:50
                        # beginLesson = f"⏱| {data[i]['beginLesson']} - {data[i]['endLesson']}"
                        # Методы принятия управленческих решений (Лек)
                        # discipline = f"<b>{data[i]['discipline']}</b> ({data[i]['kindOfWork'][0:3:]})"
                        # добавить препод
                        auditorium = f"{data[i]['auditorium']} - {data[i]['lecturer']}"

                        text.append(beginLesson)
                        text.append(discipline)
                        text.append(auditorium)
                    # Как только прошли весь цикл for добавляем 1 к переменной i
                    i += 1
                    # TODO: Добавить вывод в return
                text = ' \n'.join(text)
            return f"""{jsondate} {text}"""
        # Ловим ошибку если не смогли получить данные с JSONz
        except JSONDecodeError:
            print('Ответ не удалось обработать')
    # Ловим ошибку если сайт не доступен ошибка 404 или 401, 500
    else:
        print("Сайт не доступен")


def data_changing(date):
    date_week = datetime.date.weekday(date)
    date_monday_unclean = date - datetime.timedelta(date_week)
    date_sunday_unclean = date_monday_unclean + datetime.timedelta(days=6)
    return date_monday_unclean, date_sunday_unclean
