FROM python:3.7-slim-bullseye

WORKDIR /celery_app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD celery -A tasks worker  --loglevel=INFO
