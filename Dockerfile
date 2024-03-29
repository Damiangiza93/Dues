FROM python:3.8

RUN mkdir /app
WORKDIR /app
ADD . /app/

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/

RUN pip install -r requirements.txt
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv

EXPOSE 8000
CMD gunicorn Dues.wsgi:application --bind 0.0.0.0:8000