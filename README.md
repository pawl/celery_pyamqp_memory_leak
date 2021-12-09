This repo is an attempt to reproduce a memory leak issue with Celery + pyamqp's heartbeat functionality.

More info about the memory leak: 
* [https://github.com/celery/celery/issues/5047](https://github.com/celery/celery/issues/5047)
* [https://github.com/celery/celery/issues/4843](https://github.com/celery/celery/issues/4843)

1. Start Celery and RabbitMQ by [installing docker & docker-compose](https://docs.docker.com/get-docker/) and running:
    ```sh
    docker-compose up
    ```
1. Wait until you start seeing `ConnectionResetError: [Errno 104] Connection reset by peer` error messages.
1. Run `sudo docker stats` in another terminal window to watch memory usage.
1. Watch memory usage gradually increase by 300 KB every 10 seconds. 

In this example, the `broker_heartbeat` is set to 1 and this will make RabbitMQ constantly close connections because Celery isn't responding to heartbeats fast enough. This may simulate what can happen over time when celery fails to respond to heartbeats due to high cpu usage or long running tasks.

It may also be possible to increase memory usage with a higher `broker_heartbeat` by killing RabbitMQ connections with this command:
```bash
sudo docker-compose exec rabbitmq /bin/sh -c 'rabbitmqadmin -f tsv -q list connections name | while read conn ; do rabbitmqadmin -q close connection name="${conn}" ; done'
```
