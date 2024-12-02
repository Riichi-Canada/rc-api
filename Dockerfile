FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install fastapi uvicorn

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --port 80