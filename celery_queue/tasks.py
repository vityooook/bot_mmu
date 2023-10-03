import asyncio
import datetime
from celery import Celery
from celery.schedules import crontab

from loader import bot
from data import request_schedule

app_celery = Celery('tasks', broker='redis://127.0.0.1:6379/0')
app_celery.conf.beat_schedule = {
    'check_overdue_tasks': {
        'task': 'tasks.check_overdue_tasks',
        'schedule': crontab(hour=1, minute=55)
    },
}
app_celery.conf.update(timezone='Europe/Moscow')


@app_celery.task(name='tasks.check_overdue_tasks')
def notification_of_lessons():
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    date = datetime.date.strftime(tomorrow, '%Y.%m.%d')
    massage = request_schedule.request_schedule('487961820', date)
    asyncio.run(send_message(massage=massage))


async def send_message(massage):
    await bot.send_message(chat_id='487961820', text=massage)


# asyncio.run(send_message())