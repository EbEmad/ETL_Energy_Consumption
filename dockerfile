FROM python:3.8

WORKDIR /app

# Copy the correct requirements.txt file
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Ensure the correct paths
COPY ETL/ /app/etl
COPY data/ /app/data
COPY wait-for-postgres.sh /app/wait-for-postgres.sh
RUN chmod +x /app/wait-for-postgres.sh

ENTRYPOINT [ "/app/wait-for-postgres.sh", "pgdatabase", "python", "/app/etl/load.py" ]
