# Django celery async result

How to run with docker:
1. docker-compose build
2. docker-compose up
3. docker-compose run web python manage.py migrate
4. docker-compose run web python manage.py celeryd

http://192.168.99.100:8000/


Task is created and result of the task will be response async util done


