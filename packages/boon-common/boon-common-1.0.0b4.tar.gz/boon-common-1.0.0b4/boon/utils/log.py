#!/usr/bin/env python3

# BoBoBo

import logging
import random


def get_logger(conf={}):
    level = conf.get('level', logging.DEBUG)
    log_file = conf.get('path', 'default-log.txt')
    form = conf.get('pattern', None)
    logger_name = conf.get('name', None)
    if logger_name is None:
        logger_name = 'default-logger-' + str(random.randint(1, 100))

    return build_logger(logger_name, level, log_file, form)


def build_logger(logger_name, level, log_file, form=None):
    if not form:
        form = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    formatter = logging.Formatter(form)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(console)
    return logger
