import os
from .settings import BASE_DIR

SECRET_KEY = 'd+mw&mscg5i&tx+#@bf+6m%e+d5z!u#!n%z-^o9u7y1felv2o&'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netology_homework_db',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}