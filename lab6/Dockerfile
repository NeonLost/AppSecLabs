FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python python-pip wget && pip install flask

ADD app.py /home/app.py
ADD log /home/log

WORKDIR /home

EXPOSE 5000
