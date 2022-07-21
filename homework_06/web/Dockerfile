FROM tiangolo/uwsgi-nginx-flask:python3.10
COPY . /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python","app.py"]


#COPY requirements.txt requirements.txt

#FROM ubuntu:la
#RUN apt-get update -qy
#FROM tiangolo/uwsgi-nginx:python3.9