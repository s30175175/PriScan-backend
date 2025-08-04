import os

from celery import Celery

celery = Celery('worker', broker=os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/0'))


@celery.task
def test_task():
    print('Celery is working!')
    return 'ok'
