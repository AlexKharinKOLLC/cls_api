import requests
from utils import (
    load_to_fifo,
    warning,
    error
)
from http import HTTPStatus
from settings import API_URL
from celery import shared_task


@shared_task(name="fetcher.fetch")
def fetch():
    try:
        data = requests.get(API_URL, params={'format': 'json'})
    except requests.HTTPError as e:
        error(e)
    finally:
        if data.status_code == HTTPStatus.OK:
            return data.content.decode("utf-8")
        else:
            warning("Bad HTTP status code - %s" % data.status_code)
            return 'asd'
    

if __name__ == "__main__":
    res = fetch.delay()
    load_to_fifo(res.get(timeout=15))




