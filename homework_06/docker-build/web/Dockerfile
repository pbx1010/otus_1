FROM tiangolo/uwsgi-nginx-flask:python3.10
COPY /web/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD ["python","app.py"]
