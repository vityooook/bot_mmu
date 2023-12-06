import datetime
from json import JSONDecodeError
from os import sep
from shlex import join
import requests

from database.crud import group, chat


def compare_discipline(data):
    # Функция которая не давала мне покоя
   pass


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
    # Проверка статуса ответа от сайта
    if response.status_code == 200:
        # Блок try так же ловим ошибки
        try:
            # Применяем содержимое JSON в data
            data = response.json()
            # Передаем data в функцию compare_discipline
            """
            A function for sorting and sorting unique str from a JSON file
            """
            # Обычнный список сюда будут записываться уникальные str
            unique_discipline = []
            text = []
            # Переменная счетчика
            i = 0
            # Цикл for для перебора получаемых данных из JSON
            for _ in data:
                # Проверка на уникальность данных из data[i]['discipline'], если str уникальная то идем дальше
                if data[i]['discipline'] not in unique_discipline:
                    # Добавляем в конец списка уникальный str из data[i]['discipline'] в список unique_discipline
                    unique_discipline.append(data[i]['discipline'])
                    text.append(data[i]['discipline'])
                    # Выводим на принт последний элемент из списка
                    print(unique_discipline[-1])
                    # Выводим на принт data[i]['auditorium'] str аудиторию
                    print(data[i]['auditorium'])
                    text.append(data[i]['auditorium'])
                    # Блок else если у нас при проверке получен не уникальный data[i]['discipline']
                else:
                    # print(data[i]['discipline']) тут я закоментил бред

                    # Выводим на принт data[i]['auditorium'] будет выводиться каждый раз когда у нас не уникальный str в data[i]['discipline']
                    print(data[i]['auditorium'])
                    text.append(data[i]['auditorium'])
                # Как только прошли весь цикл for добавляем 1 к переменной i
                i += 1
                # if not unique_discipline:
                #     text_return += 'Пар нет на указанную дату!'
                #     text_return = f"{datetime.date.strftime(datetime.datetime.now(), '%Y.%m.%d')}\n" + \
                #         text_return
                # TODO: Добавить вывод в return
            text = ', \n'.join(text)
            
            return f"""{text}"""
        # Ловим ошибку если не смогли получить данные с JSONz
        except JSONDecodeError:
            print('Ответ не удалось обработать')
    # Ловим ошибку если сайт не доступен ошибка 404 или 401, 500
    else:
        print("Сайт не доступен")


def data_changing(time_data):
    date_week = datetime.date.weekday(time_data)
    date_monday_unclean = time_data - datetime.timedelta(date_week)
    date_sunday_unclean = date_monday_unclean + datetime.timedelta(days=6)
    return date_monday_unclean, date_sunday_unclean
