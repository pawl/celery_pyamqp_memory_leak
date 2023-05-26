import logging
from time import sleep

from celery import Celery

app = Celery('tasks', broker='redis://redis:6379/0', worker_prefetch_multiplier=1, task_acks_late=True, worker_max_tasks_per_child=100)

@app.task()
def add(x, y):
    return x + y
