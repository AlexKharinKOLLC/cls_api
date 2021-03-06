import settings
import simplejson
from kombu import Connection


def queue_init(func):
    def inner(*args, **kwargs):
        connection = Connection(settings.BROKER_URL)
        connection.connect()

        queue = connection.SimpleQueue(settings.QUEUE_NAME)
        res = func(*args, **kwargs, queue=queue)
        connection.release()
        return res
    return inner


@queue_init
def write_in_queue(data, queue=None):
    try:
        queue.put(data, routing_key=settings.ROUTING_KEY)
    except Exception as e:
        print(e)


@queue_init
def read_from_queue(queue=None):
    data = []
    try:
        for _ in range(queue.qsize()):
            msg = queue.get(block=False, timeout=5)
            if msg:
                data.append(simplejson.loads(msg.body))
                msg.ack()
            else:
                break
    except Exception as e:
        print(e)

    return data
