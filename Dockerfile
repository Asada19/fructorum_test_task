FROM python:3.8.16

ENV PYTHONUNBUFFERED 1

RUN mkdir /Bookmark

WORKDIR /Bookmark

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
