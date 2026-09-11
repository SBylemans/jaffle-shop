from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

default_args = {
  'owner': 'data-team',
  'start_date': datetime(2024, 1, 1),
  'retries': 1
}

with DAG('data_pipeline', default_args=default_args, schedule='@daily', catchup=False) as dag:
  run = DockerOperator(
          task_id = 'dbt_build',
          image='ghcr.io/sbylemans/jaffle-shop:latest',
          command='build --profiles-dir /dbt',
          docker_url='unix://var/run/docker.sock',
          network_mode='escape-room',
          environment={
            'PGHOST': 'postgres',
            'PGPORT': '5432',
            'PGUSER': 'jaffle',
            'PGPASSWORD': 'jaffle',
            'PGDATABASE': 'jaffle',
          },
          auto_remove='force',
        )
