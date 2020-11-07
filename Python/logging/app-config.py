import logging
import logging.config


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'normal': {  # the name of formatter
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'simple': {  # the name of formatter
            'format': '%(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console1': {  # the name of handler
            'class': 'logging.StreamHandler',  # emit to sys.stderr(default)
            'formatter': 'normal',  # use the above "normal" formatter
        },
        'console2': {  # the name of handler
            'class': 'logging.StreamHandler',  # emit to sys.stderr(default)
            'formatter': 'simple',  # use the above "simple" formatter
        },
        'file1': {  # the name of handler
            'class': 'logging.FileHandler',  # emit to disk file
            'filename': 'f1.log',  # the path of the log file
            'formatter': 'normal',  # use the above "normal" formatter
        },
        'file2': {  # the name of handler
            'class': 'logging.FileHandler',  # emit to disk file
            'filename': 'f2.log',  # the path of the log file
            'formatter': 'simple',  # use the above "simple" formatter
        },
        'time-rotating-file': {  # the name of handler
            'class': 'logging.handlers.TimedRotatingFileHandler',  # the log rotation by time interval
            'filename': 'f3.log',  # the path of the log file
            'when': 'midnight',  # time interval
            'formatter': 'normal',  # use the above "simple" formatter
        },
    },
    'loggers': {
        'c': {  # the name of logger
            'handlers': ['console1', 'console2'],  # use the above "console1" and "console2" handler
            'level': 'INFO',  # logging level
        },
        'f1': {  # the name of logger
            'handlers': ['file1'],  # use the above "file1" handler
            'level': 'INFO',  # logging level
            'propagate': True,
        },
        'f2': {  # the name of logger
            'handlers': ['file2'],  # use the above "file2" handler
            'level': 'INFO',  # logging level
            'propagate': True,
        },
        'time-f': {  # the name of logger
            'handlers': ['time-rotating-file'],  # use the above "time-rotating-file" handler
            'level': 'INFO',  # logging level
            'propagate': True,
        },
    },
}

logging.config.dictConfig(config=LOGGING)


if __name__ == "__main__":
    logger_c = logging.getLogger('c')
    logger_c.info('info')

    logger_f1 = logging.getLogger('f1')
    logger_f1.info('info')

    logger_f2 = logging.getLogger('f2')
    logger_f2.info('info')

    logger_time_f = logging.getLogger('time-f')
    logger_time_f.info('info')
