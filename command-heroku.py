# https://hub.docker.com/

echo web: gunicorn django1.wsgi --log-file - > Procfile

echo python-3.8.10 > runtime.txt

pip install django-heroku

pip install gunicorn

pip freeze > requirements.txt

sudo apt install cloud-init

# config\settings.py
DEBUG = False

ALLOWED_HOSTS = ['*']

heroku login -i
heroku git:remote -a APPNAME
heroku config:set DISABLE_COLLECTSTATIC=1
git push heroku master
