from time import sleep

from tasks import app, add

while True:
    add.apply_async([1, 2])
    print('task queued')
    sleep(.1)
