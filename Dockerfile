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


ENTRYPOINT ["airflow", "db", "upgrade"]

FROM builder AS production

