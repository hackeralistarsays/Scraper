import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
SECRET_KEY = 'nwv@ceib0!7mrkx!m-fg*&(5+7(iwvfp#%z=*86fm^zh+r8xg8'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database.sqlite3'),
    }
}


# Email confirmation configurations 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ibrentone.alistar@gmail.com'
EMAIL_HOST_PASSWORD = 'ArcadiaComplex'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER