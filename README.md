This branch is an attempt to reproduce Celery workers getting stuck while using Redis as a broker. More info: https://github.com/celery/celery/discussions/7276

This branch is also testing mbierma's kombu fix here: https://github.com/celery/kombu/pull/1733

1. Run `git submodule update --init --recursive` to get submodules.
1. Start Celery and Redis by [installing docker & docker-compose](https://docs.docker.com/get-docker/) and running:
    ```sh
    docker-compose up
    ```
1. In another terminal window, restart redis with `docker-compose restart redis`.
1. Repeatedly restart redis until it gets stuck and no longer processes tasks.
