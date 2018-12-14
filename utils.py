import os
import errno
import settings
import tempfile
import logging.handlers
import pika


def logger_init(func):
    def inner(data):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        handler = logging.handlers.SysLogHandler(address='/dev/log')
        logger.addHandler(handler)
        
        return func(data, logger)
    return inner

    
@logger_init
def warning(data, logger=None):
    if logger:
        logger.debug("WARNING: %s" % data)


@logger_init
def error(data, logger=None):
    if logger:
        logger.debug("ERROR: %s" % data)


def load_to_fifo(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='cls')

    channel.basic_publish(exchange='',
                          routing_key='cls',
                          body=data)
    connection.close()


def read_from_fifo():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='cls')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(callback,
                          queue='cls',
                          no_ack=True)
    channel.start_consuming()
    connection.close()
