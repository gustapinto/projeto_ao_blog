FROM python:3.9

WORKDIR /blog

COPY ./requirements.txt /blog/requirements.txt

RUN pip3 install -r requirements.txt