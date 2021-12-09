import logging

from celery import Celery

app = Celery('tasks', broker='amqp://guest@rabbitmq//', broker_heartbeat=1)

@app.task()
def add(x, y):
    return x + y
