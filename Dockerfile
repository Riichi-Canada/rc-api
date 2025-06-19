FROM python:3.13

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]