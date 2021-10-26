import logging
import os

from cryptocurrency.settings import DEBUG, BASE_DIR

log = logging.getLogger(__name__)

if DEBUG:
    min_level = 'DEBUG'
else:
    min_level = 'INFO'

min_django_level = 'INFO'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # keep Django's default loggers
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'timestampthread': {
            'format': "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] [%(name)-20.20s]  %(message)s",
        },
    },
    'handlers': {
        'logfile': {
            # optionally raise to INFO to not fill the log file too quickly
            'level': min_level,  # this level or higher goes to the log file
            'class': 'logging.handlers.RotatingFileHandler',
            # IMPORTANT: replace with your desired logfile name!
            'filename': os.path.join(BASE_DIR, 'djangoproject.log'),
            'maxBytes': 50 * 10 ** 6,  # will 50 MB do?
            'backupCount': 3,  # keep this many extra historical files
            'formatter': 'timestampthread'
        },
        'console': {
            'level': min_level,  # this level or higher goes to the console
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {  # configure all of Django's loggers
            'handlers': ['logfile', 'console'],
            'level': min_django_level,  # this level or higher goes to the console
            'propagate': False,  # don't propagate further, to avoid duplication
        },
        '': {
            'handlers': ['logfile', 'console'],
            'level': min_level,  # this level or higher goes to the console,
        },
    },
}
