import requests
from utils import load_to_fifo
from http import HTTPStatus
from settings import API_URL
from celery import shared_task


@shared_task(name="fetcher.fetch")
def fetch():
    try:
        data = requests.get(API_URL, params={'format': 'json'})
    except requests.HTTPError as e:
        print(e)
    finally:
        if data.status_code == HTTPStatus.OK:
            load_to_fifo(data.content.decode("utf-8"))
            print("Data fetched")
        else:
            print("WARNING: Bad HTTP status code - %s" % data.status_code)
    

if __name__ == "__main__":
    fetch.delay()



