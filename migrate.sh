#!/bin/bash

cd /app/ || exit

/opt/venv/bin/python manage.py migrate --noinput
/opt/venv/bin/python manage.py collectstatic --noinput
/opt/venv/bin/python manage.py createsuperuser --noinput || true
