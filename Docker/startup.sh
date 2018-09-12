#!/bin/bash
sleep 5
usr/sbin/httpd &
cd /home/java/app/YaKan
uwsgi --ini uwsgi.ini
#python3.6 manage.py createsuperuser
python3.6 manage.py makemigrations
python3.6 manage.py migrate
python3.6 manage.py runworker --settings YaKan.settings channels &
daphne -b 0.0.0.0 -p 8001 YaKan.asgi:application

