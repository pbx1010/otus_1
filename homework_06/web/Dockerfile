FROM ubuntu:latest
RUN apt-get update -qy
FROM tiangolo/uwsgi-nginx:python3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]


