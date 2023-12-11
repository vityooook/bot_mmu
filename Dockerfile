FROM python:3.10-slim-bullseye as production

COPY . /app

WORKDIR app

RUN pip install -r requirements.txt

ENV TOKEN=placeholder


ENTRYPOINT ["python3", "main_tg.py"]