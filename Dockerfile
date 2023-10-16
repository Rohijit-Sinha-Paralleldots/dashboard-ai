FROM python:3.10.2-slim-bullseye

RUN apt-get update\
    && apt-get upgrade -y\
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip\
    && pip install -r requirements.txt

COPY . .

CMD [ "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000", "--reload" ]