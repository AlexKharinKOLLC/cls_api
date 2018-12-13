import os
import errno
import settings
import tempfile
import logging.handlers

FIFO = os.path.join(tempfile.gettempdir(), settings.FIFO_NAME)


def logger_init(func):
    def inner(data):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        handler = logging.handlers.SysLogHandler(address='/dev/log')
        logger.addHandler(handler)
        
        return func(data, logger)
    return inner

    
@logger_init
def warning(data, logger):
    logger.debug("WARNING: %s" % data)


@logger_init
def error(data, logger):
    logger.debug("ERROR: %s" % data)


def load_to_fifo(data):
    with open(FIFO, 'a') as file:
        file.write("%s\n" % data)


def read_from_fifo():
    if not os.path.exists(FIFO):
        return []
    
    data = []
    with open(FIFO, 'r') as file:
        for line in file:
            data.append(line)
    os.remove(FIFO)
    return data
