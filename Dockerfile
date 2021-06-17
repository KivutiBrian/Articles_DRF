# pull official base image
FROM python:3.8.5-alpine

# set work directory
WORKDIR /src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 #Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1 #Prevents Python from buffering stdout and stderr

# upgrade pip

RUN pip install --upgrade pip

COPY ./requirements.txt .

# install requirements file
RUN pip install -r requirements.txt

# install system required dependencies
# RUN apt-get update && apt-get install --no-install-recommends -y \
#     default-libmysqlclient-dev \
#     default-mysql-client -y 

COPY . /app


