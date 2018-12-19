import requests
from queue_utils import write_in_queue
from http import HTTPStatus
from settings import API_URL
from celery import shared_task


@shared_task(name="fetcher.fetch", time_limit=10)
def fetch():
    try:
        data = requests.get(API_URL, params={'format': 'json'})
    except requests.HTTPError as e:
        print(e)
    finally:
        if data.status_code == HTTPStatus.OK:
            write_in_queue(data.content.decode("utf-8"))
            print("Data fetched")
        else:
            print("WARNING: Bad HTTP status code - %s" % data.status_code)
    

if __name__ == "__main__":
    fetch.delay()



