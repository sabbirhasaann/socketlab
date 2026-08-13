import os
from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG_DEV') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS_DEV', 'localhost').split(',')

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('ENGINE_DEV'),
        'NAME': Path.joinpath(BASE_DIR, os.environ.get('NAME_DEV')),
    }
}


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": os.environ.get('REDIS_CHANNEL'),
        "CONFIG": {
            "hosts": [{
                "address": "redis://127.0.0.1:6379/0",
                "socket_timeout": 10,
                "socket_connect_timeout": 5,
            }],
        }
    }
}
