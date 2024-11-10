from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    'example_postgres_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Создаем таблицу
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='my_db',  # ID подключения к Postgres
        sql="""
        CREATE TABLE IF NOT EXISTS my_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """,
    )

    # Вставляем данные
    insert_data = PostgresOperator(
        task_id='insert_data',
        postgres_conn_id='my_db',
        sql="INSERT INTO my_table (name) VALUES ('example');",
    )

    # Получаем данные
    select_data = PostgresOperator(
        task_id='select_data',
        postgres_conn_id='my_db',
        sql="SELECT * FROM my_table;",
    )

    create_table >> insert_data >> select_data