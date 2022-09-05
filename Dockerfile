FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONONBUFFERED 1

WORKDIR /code

COPY requirments.txt /code/
RUN pip install -r requirments.txt

COPY . /code/