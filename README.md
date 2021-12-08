This repo is an attempt to reproduce a memory leak issue with celery + pyamqp's heartbeat functionality: [https://github.com/celery/celery/issues/5047](https://github.com/celery/celery/issues/5047)

Start celery and rabbitmq by [installing docker & docker-compose](https://docs.docker.com/get-docker/) and running:
```sh
docker-compose up
```

1. Run `sudo ./restart_rabbitmq.sh`
1. You should start to see "ConnectionResetError: [Errno 104] Connection reset by peer" errors occasionally in the console.
1. Run `sudo docker stats` in another terminal window to watch memory usage.
1. Watch memory usage slowly grow
