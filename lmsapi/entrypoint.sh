#!/bin/sh

# Tohle na vzcisti tabulky VSECHNY ktere jsou management!!!!!
#python manage.py flush --no-input

python manage.py migrate
gunicorn core.wsgi:application --bind 0.0.0.0:80

exec "$@"
