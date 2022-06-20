FROM python:3.10.5-slim-bullseye

RUN apt-get update && python -m pip install --upgrade pip && python -m pip install redis==4.3.3 Flask==2.1.2
COPY ./__main__.py /usr/src/__main__.py