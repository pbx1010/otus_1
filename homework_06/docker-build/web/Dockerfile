#FROM tiangolo/uwsgi-nginx-flask:python3.10
#
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#
#copy .web /app


#COPY requirements.txt requirements.txt

#FROM ubuntu:la
#RUN apt-get update -qy
#FROM tiangolo/uwsgi-nginx:python3.9

FROM tiangolo/uwsgi-nginx-flask:python3.10


# WORKDIR /app

COPY /web/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app


CMD ["python","app.py"]