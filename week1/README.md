# WEEK1

## Docker
### Basic
1. Create dockerfile:
```Dockerfile
FROM python:3.9.1
RUN pip install pandas
WORKDIR /app
ENTRYPOINT ["bash"]
```
2. Build image
 ```bash
docker build -t test:latest .
```
3. Enter the docker environment
```bash
docker run -it test
```
### Pass arguments into the container
Docker file
```Dockerfile
FROM python:3.9.1
RUN pip install pandas
WORKDIR /app
COPY pipeline.py pipeline.py
ENTRYPOINT [ "python", "pipeline.py" ]
```
Python
```python
import sys
import pandas as pd
print(sys.argv)
day = sys.argv[1]
print(f'this is a pipeline built in {day}')
```
## Ingesting NY Taxi Data to Postgres
```bash
docker run -it \
  -e POSTGRES_USER="root"  \
  -e POSTGRES_PASSWORD="root"  \
  -e POSTGRES_DB="ny_taxi"  \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```
## Access the database
pgcli
```bash
pgcli -h localhost -p 5432 -u root -d ny_taxi
```
## Preview the data 
### CSV
- Preview the file
```bash
less 'file_name'
```
- Save first 100 to a new csv file
```bash
head -n 100 'file_name.csv' > 'partial_file_name.csv'
```
- Count the number of lines
```bash
wc -l 'file_name'
```
### parquet


### Set the kernel of jupyter notebook 
```bash
ipython kernel install --name 'virtual_env_name' --user
```
## Put the data to database
### Set the env of jupyter notebook
```bash
ipython kernel install --name 'virtual_env_name' --user
```
Check w1_upload_data

## PgAdmin
```bash
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4
```

## Connect postgres with pg admin
Connect 2 dockers by setting the network
https://docs.docker.com/engine/reference/commandline/network_create/
```bash
docker network create pg-network
```
connect to postgres
```bash
docker run -it \
  -e POSTGRES_USER="root"  \
  -e POSTGRES_PASSWORD="root"  \
  -e POSTGRES_DB="ny_taxi"  \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13
```
connect to pgadmin
```bash
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin \
  dpage/pgadmin4
```