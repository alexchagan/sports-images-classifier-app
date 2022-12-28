FROM tensorflow/tensorflow:latest

WORKDIR /usr/src/app

COPY . .

RUN mkdir /usr/src/app/static

RUN pip install --upgrade pip && pip install flask gunicorn 

RUN apt-get update

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 predictor:app



