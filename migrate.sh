#!/bin/bash

cd /app/ || exit

/opt/venv/bin/python manage.py migrate --noinput || true
/opt/venv/bin/python manage.py collectstatic --noinput || true
/opt/venv/bin/python manage.py createsuperuser --noinput || true
