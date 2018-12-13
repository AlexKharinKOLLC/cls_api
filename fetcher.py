import requests
from utils import (
    load_to_fifo,
    warning,
    error
)
from http import HTTPStatus
from settings import (
    API_URL
)


def fetch():
    try:
        data = requests.get(API_URL, params={'format': 'json'})
    except requests.HTTPError as e:
        error(e)
    finally:
        if data.status_code == HTTPStatus.OK:
            load_to_fifo(data.content.decode("utf-8"))
        else:
            warning("Bad HTTP status code - %s" % data.status_code)


if __name__ == "__main__":
    fetch()




