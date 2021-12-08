This repo is an attempt to reproduce a memory leak issue with celery + pyamqp's heartbeat functionality: [https://github.com/celery/celery/issues/5047](https://github.com/celery/celery/issues/5047)

Start celery and rabbitmq by [installing docker & docker-compose](https://docs.docker.com/get-docker/) and running:
```sh
docker-compose up
```

1. Run `sudo docker stats` in another terminal window to watch memory usage.
1. Write down the current memory usage of the `example_celery_celery_1` container.
1. Visit this url: [http://localhost:15672/#/connections](http://localhost:15672/#/connections)
1. Click the active connection.
1. Click "force close" at the bottom of the page for the active connection.
1. Observe the "amqp.exceptions.RecoverableConnectionError: Socket was disconnected" error message generated by closing the connection.
1. Compare the memory usage to the memory usage you wrote down in previous steps.
1. Repeat to increase memory usage.

