FROM python:3.9-slim-bullseye as production

WORKDIR app

COPY . /app

CMD ["python3", "-c", "print('Hello world')"]