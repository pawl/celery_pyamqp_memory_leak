This repo is an attempt to reproduce a memory leak issue with Celery + pyamqp's inspect functionality.

More info about the memory leak: 
* [https://github.com/celery/celery/issues/6009](https://github.com/celery/celery/issues/6009)

1. Run `git submodule update --init --recursive` to get submodules.
1. Start Celery and RabbitMQ by [installing docker & docker-compose](https://docs.docker.com/get-docker/) and running:
    ```sh
    docker-compose up
    ```
1. Watch the tracemalloc output from the celery-stats_1 container for increasing memory usage.
