import logging
from time import sleep

from celery import Celery

app = Celery('tasks', broker='redis://redis:6379/0')

@app.task()
def add(x, y):
    return x + y
