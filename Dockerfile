FROM python:3.10-slim-bullseye as production

WORKDIR app

RUN pip install --no-cache-dir -r ./requirements.txt

COPY . .