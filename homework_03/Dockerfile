
FROM python:3.9.12-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install poetry==1.1.13
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY blogproject .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
