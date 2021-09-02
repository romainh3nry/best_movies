FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django-bestMovies

COPY Pipfile Pipfile.lock /django-bestMovies/
RUN pip install pipenv && pipenv install --system

COPY . /django-bestMovies/