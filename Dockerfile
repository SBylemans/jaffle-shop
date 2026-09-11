FROM python:3.12-slim
RUN pip install --no-cache-dir dbt-postgres
WORKDIR /dbt
COPY . .
RUN dbt deps --no-send-anonymous-usage-stats
ENTRYPOINT ["dbt"]
