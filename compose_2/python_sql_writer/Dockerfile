FROM python:3.9-slim
WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2 pymongo redis
CMD ["python", "write_data.py"]

