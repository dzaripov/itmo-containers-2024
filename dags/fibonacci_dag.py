from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import numpy as np


def compute_fibonacci(n_terms: int):
    if n_terms < 2:
        return []
    fib_sequence = np.zeros(n_terms, dtype=int)
    fib_sequence[0] = 0
    fib_sequence[1] = 1
    for i in range(2, n_terms):
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]
    fib_list = fib_sequence.tolist()
    print(f"Fibonacci sequence up to {n_terms} terms: {fib_list}")
    return fib_list


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'catchup': False
}

with DAG(
    dag_id='fibonacci_dag_with_numpy',
    default_args=default_args,
    schedule=None,
    description='A DAG to compute Fibonacci sequence using NumPy',
    tags=['fibonacci', 'numpy']
) as dag:

    fibonacci_task = PythonOperator(
        task_id='compute_fibonacci',
        python_callable=compute_fibonacci,
        op_args=[10000],
    )

    fibonacci_task
