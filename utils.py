import settings
import pika
from pika.spec import Basic


def queue_init(func):
    def inner(*args, **kwargs):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        res = func(*args, **kwargs, channel=channel)
        connection.close()
        return res
    return inner


@queue_init
def load_to_fifo(data, channel=None):
    if not channel:
        return

    channel.queue_declare(queue=settings.QUEUE_NAME)

    channel.basic_publish(exchange='',
                          routing_key=settings.QUEUE_NAME,
                          body=data)


@queue_init
def read_from_fifo(channel=None):
    if not channel:
        return []

    data = []
    while True:
        code, props, body = channel.basic_get(queue=settings.QUEUE_NAME, no_ack=True)
        if isinstance(code, Basic.GetOk):
            data.append(body)
        else:
            break

    return data
