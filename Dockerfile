FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir dbt-postgres
WORKDIR /dbt
COPY . .
RUN dbt deps --no-send-anonymous-usage-stats
ENTRYPOINT ["dbt"]
