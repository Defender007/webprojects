from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='acp)ye@+36+^036asil(rt=*00-ej_x0%_j_hu!67ifetbp!ed')
DEBUG = env.bool('DJANGO_DEBUG', True)

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'mysql.connector.django',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'webproject_data',
        # 'NAME': str(ROOT_DIR.path('db.sqlite3')),
        'USER': 'django_user',
        # 'USER': 'obitexlocal_usr',
        'PASSWORD': env('DATABASE_PWORD', default='sQlqwerty123$*'),
        'HOST': '127.0.0.1',
        'PORT': '',
        'init_command': 'SET default_storage_engine=INNODB',  # this must be removed after the table has been created
        'OPTIONS': {}


    }
}
