from utils import load_to_fifo
import requests
from settings import (
    API_URL
)


def fetch():
    data = requests.get(API_URL, params={'format': 'json'})
    load_to_fifo(data.content)


if __name__ == "__main__":
    fetch()



