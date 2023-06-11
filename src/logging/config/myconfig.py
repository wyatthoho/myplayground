LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s:%(name)s:%(message)s'
        }
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'main': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
        'main.lib': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}
