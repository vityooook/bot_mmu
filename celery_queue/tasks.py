import asyncio
import datetime
import logging

from celery import Celery
from celery.schedules import crontab
from aiogram.enums.parse_mode import ParseMode

from loader import bot
from data import request_schedule


logging.basicConfig(format=u'%(filename)s:%(lineno)-d #%(levelname)-16s [%(asctime)s] %(message)s',
                    level=logging.INFO)
app_celery = Celery('tasks', broker='redis://127.0.0.1:6379/0', )


@app_celery.task(name='tasks.add')
def send_schedule_daily():
    print('i start work')
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    massage = request_schedule.request_schedule(user_id=487961820, time_data=tomorrow)
    asyncio.get_event_loop().run_until_complete(
        bot.send_message(chat_id=487961820, text=massage, parse_mode=ParseMode.HTML))
    print(globals())
    logging.info(globals())


app_celery.conf.beat_schedule = {
    'notifications': {
        'task': 'tasks.add',
        'schedule': crontab()
    },
}
app_celery.conf.update(timezone='Europe/Moscow')
app_celery.config_from_object('')
# app_celery.config_from_envvar()


if __name__ == '__main__':
    app_celery.worker_main(["-A", "celery_queue.tasks", "worker", "-B"])