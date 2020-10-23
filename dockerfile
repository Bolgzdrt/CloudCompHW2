FROM python:3.8

COPY . /home
WORKDIR /home

CMD [ "python", "./app.py" ]