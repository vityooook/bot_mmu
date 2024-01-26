import datetime
from loguru import logger
from json import JSONDecodeError
import requests
# * import db SQL commands
from database.crud import user


@logger.catch()
async def get_day_schedule(user_id: int, date: datetime) -> str:
    """ make a request to the university's API to get the schedule for a specific day


    :param user_id: student's user id of Telegram
    :param date: date for API

    :return: schedule for day
    """
    logger.debug("getting the daily schedule")
    # * get user's group id
    group_id = await user.get_user_group_id(user_id)
    # * conversion from datetime format to str
    date_str = date.strftime("%Y.%m.%d")
    # * make a request to the university's API
    response = requests.get(
        f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
        f"{group_id}?start={date_str}&finish={date_str}&lng=1"
    )
    # * checking connection to the API
    if response.status_code == 200:
        try:
            # * conversion from requests format to json
            data = response.json()
            # * if data is empty, return message
            if not data:
                text = "Пар нету! кайфуем 😸"
                return text
            else:
                # * a tuple with uniq elements
                unique_combinations = set()
                text = []
                for entry in data:
                    # * create a tuple with elements
                    combination = (entry["discipline"], entry["beginLesson"])
                    # * check the uniqueness of elements
                    if combination not in unique_combinations:
                        # * adding unique elements to a unique tuple
                        unique_combinations.add(combination)
                        # * generate the schedule text
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
                        # * if subject not uniq, add only auditorium and lecturer
                        auditorium_info = f"{entry['auditorium']} - {entry['lecturer']}"
                        text.append(auditorium_info)
                text = "\n".join(text)
                # * return schedule
                return f"{json_date}{text}"
        except JSONDecodeError as error:
            logger.exception(f"Ошибка декодирования JSON {error}")
    else:
        logger.error(f"Ошибка: {response.status_code}")


@logger.catch()
async def get_week_schedule(user_id: int, date: datetime):
    """ Make a request to the university's API to get the schedule for a week.

    :param user_id: The student's user id of Telegram.
    :param date: The date for the API request.
    :return: The schedule for the week.
    """

    # * get group id for API
    group_id = await user.get_user_group_id(user_id)

    # * find first day and last day of week for API
    date_monday_unclean, date_sunday_unclean = data_changing(date)
    date_monday = datetime.date.strftime(date_monday_unclean, "%Y.%m.%d")
    date_sunday = datetime.date.strftime(date_sunday_unclean, "%Y.%m.%d")

    # * make a request to the university's API
    response = requests.get(
        f"https://mmu2021:mmu2021@schedule.mi.university/api/schedule/group/"
        f"{group_id}?start={date_monday}&finish={date_sunday}&lng=1"
    )
    # * checking connection to the API
    if response.status_code == 200:
        try:
            # * conversion from requests format to json
            data = response.json()
            # * if data is empty, return message
            if not data:
                text = "На этой неделе пар нету! кайфуем 😸"
                return text
            else:
                # * a tuple with uniq elements
                unique_days = set()
                unique_combinations = set()
                text = []
                for entry in data:
                    # * create a tuple with elements
                    current_day = entry["date"]
                    combination = (entry["discipline"], entry["beginLesson"], current_day)

                    if current_day not in unique_days:
                        unique_days.add(current_day)
                        json_date = (
                            f"\n–––––––––––––––––––––––––––––"
                            f"\n{entry['dayOfWeekString']} (<b>{current_day}</b>)\n"
                        )
                        text.append(json_date)
                    # * check the uniqueness of elements
                    if combination not in unique_combinations:
                        # * adding unique elements to a unique tuple
                        unique_combinations.add(combination)
                        # * generate the schedule text
                        begin_lesson = (
                            f"\n⏱| {entry['beginLesson']} - {entry['endLesson']}"
                        )
                        discipline = f"<b>{entry['discipline']}</b> ({entry['kindOfWork'][0:3:]})"
                        auditorium = f"{entry['auditorium']} - {entry['lecturer']}"

                        text.extend([begin_lesson, discipline, auditorium])
                    else:
                        # * if subject not uniq, add only auditorium and lecturer
                        auditorium_info = f"{entry['auditorium']} - {entry['lecturer']}"
                        text.append(auditorium_info)
            # * return schedule
            return "\n".join(text)
        except JSONDecodeError as error:
            logger.exception(f"Ошибка декодирования JSON {error}")
    else:
        logger.error(f"Ошибка: {response.status_code}")


def data_changing(date: datetime):
    date_week = datetime.date.weekday(date)
    date_monday_unclean = date - datetime.timedelta(date_week)
    date_sunday_unclean = date_monday_unclean + datetime.timedelta(days=6)
    return date_monday_unclean, date_sunday_unclean
