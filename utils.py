import os
import errno
import settings
import tempfile

FIFO = os.path.join(tempfile.gettempdir(), settings.FIFO_NAME)


def load_to_fifo(data):
    with open(FIFO, 'a') as file:
        file.write("\nData - %s\n" % data)


def read_from_fifo():
    data = []
    with open(FIFO, 'r') as file:
        for line in file:
            data.append(line)
    os.remove(FIFO)
    return data
