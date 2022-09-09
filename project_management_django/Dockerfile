FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code/project_management_django
COPY . /code/

RUN pip install -r requirements.txt