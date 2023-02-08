FROM python:3.10-slim

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

WORKDIR /app

RUN apt-get update

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]