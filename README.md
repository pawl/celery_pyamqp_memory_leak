This branch is an attempt to reproduce a memory leak issue with Celery + redis.

More info about the memory leak: 
* [https://github.com/celery/celery/issues/5047](https://github.com/celery/celery/issues/5047)
* [https://github.com/celery/celery/issues/4843](https://github.com/celery/celery/issues/4843)

1. Run `git submodule update --init --recursive` to get submodules.
1. Start Celery and Redis by [installing docker & docker-compose](https://docs.docker.com/get-docker/) and running:
    ```sh
    docker-compose up
    ```
1. Wait until the worker finishes starting. You should see a "basic.qos: prefetch_count->32" message after a few seconds.
1. Restart redis with `docker-compose restart redis`.
1. Wait until you see a `ConnectionError` and find the "Top 10 lines" output to see memory usage increase on specific lines of code.
1. Repeatedly restart redis to see memory usage continue to increase.

In this example, restarting redis will trigger a `ConnectionError` and somehow this results in the kombu `Transport` not getting cleaned up by garbage collection. This may simulate what can happen over time when celery fails to redis due to connectivity issues.

Maybe this is a similar issue to the one Michael Lazar fixed in: [https://github.com/celery/py-amqp/pull/374](https://github.com/celery/py-amqp/pull/374) And maybe we have an unclosed socket still?
