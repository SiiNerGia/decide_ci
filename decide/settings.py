import os
import django_heroku
...
BASEURL = 'http://heroku-meet-travis.herokuapp.com'

APIS = {
    'authentication': BASEURL,
    'base': BASEURL,
    'booth': BASEURL,
    'census': BASEURL,
    'mixnet': BASEURL,
    'postproc': BASEURL,
    'store': BASEURL,
    'visualizer': BASEURL,
    'voting': BASEURL,
}

...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'decide',
        'USER': 'decide',
        'PASSWORD': 'decide',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
...
INSTALLED_APPS = INSTALLED_APPS + MODULES
django_heroku.settings(locals())
4) Preparamos y añadimos al repositorio el Procfile para Heroku

% prepara el repositorio para su despliegue. 
release: sh -c 'cd decide && python manage.py migrate'
% especifica el comando para lanzar Decide
web: sh -c 'cd decide && gunicorn decide.wsgi --log-file -'