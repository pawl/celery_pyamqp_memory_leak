from time import sleep

from tasks import app, add

while True:
    add.apply_async([1, 2])
    sleep(1)
