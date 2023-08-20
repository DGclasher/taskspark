# TaskSpark

## Description

A simple todo list API using graphQL

## Deployment

### Using Docker Compose

Get the `docker-compose.yml`
```
wget https://github.com/DGclasher/taskspark/raw/deployment/docker-compose.yml
```

Create a `.env` file at same location as `docker-compose.yml`
```
DEBUG=1

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=postgres_db
DB_PORT=6432

DJANGO_SUPERUSER_USERNAME=
DJANGO_SUPERUSER_EMAIL=
DJANGO_SUPERUSER_PASSWORD=

SECRET_KEY=
```

Bring up the services
```
sudo docker-compose up -d
```

Application can be accessed at port `8001`

###