import os
from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": os.environ.get('REDIS_CHANNEL'),
        "CONFIG": {
            "hosts": [(os.environ.get('REDIS_HOST'), os.environ.get('REDIS_PORT'))],
        }
    }
}
