# django-chart
simple graph application based on django-graphos

This application plot graphs using django-graphos. This application use many to many field models. Please load json file before running.
#Usage
pip install django-graphos

manage.py loaddata User1000.json

manage.py loaddata VideoData.json

manage.py loaddata link_User1000.json

manage.py syncdb

manage.py makemigrations

manage.py migrate

manage.py runserver
