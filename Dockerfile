FROM python:3.7-slim-bullseye

WORKDIR /celery_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD celery -A tasks worker --loglevel=DEBUG --without-gossip --without-heartbeat
