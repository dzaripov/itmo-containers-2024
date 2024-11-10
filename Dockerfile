FROM apache/airflow:slim-2.10.3-python3.11 AS builder

USER root
RUN apt-get update && apt-get install -y \
    vim \
    curl \
    wget \
    && apt-get clean

USER airflow

COPY requirements.txt /opt/airflow/requirements.txt

RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt




FROM builder AS initializer


# Выполняем команду инициализации базы данных Airflow
ENTRYPOINT ["airflow", "db", "upgrade"]
# Можно также добавить команду для создания пользователя-администратора:
# RUN airflow users create -u admin -p admin -r Admin -e admin@example.com -f Admin -l User

FROM builder AS production


# USER airflow

ENTRYPOINT ["airflow", "webserver"]