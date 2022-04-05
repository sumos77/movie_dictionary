# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-b", ":5000", "app:app"]
