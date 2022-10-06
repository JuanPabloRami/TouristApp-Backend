FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /touristApp
COPY ./requirements.txt .
RUN apk update
RUN apk add build-base mariadb-connector-c-dev
RUN python -m pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
