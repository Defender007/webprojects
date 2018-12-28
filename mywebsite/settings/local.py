from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='acp)ye@+36+^036asil(rt=*00-ej_x0%_j_hu!67ifetbp!ed')
DEBUG = env.bool('DJANGO_DEBUG', True)
