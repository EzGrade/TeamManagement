FROM python:3.11.9
LABEL authors="Grade"

WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip


COPY . /app

RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 8000


CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]