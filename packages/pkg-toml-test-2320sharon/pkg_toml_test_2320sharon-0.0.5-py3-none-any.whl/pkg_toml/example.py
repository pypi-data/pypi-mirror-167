import requests

def get_request():
    r = requests.get('https://api.github.com/events')
    return r.status_code


def add_one(number):
    return number + 1