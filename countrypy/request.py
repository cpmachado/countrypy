"""
    request module for project

    has base request and methods to build on
"""

from urllib.request import urlopen
import json

BASE_URL = 'https://restcountries.eu/rest/v2/'

def get_countries_base(path = 'all'):
    """
        base function to implement api access
    """
    url = f'{BASE_URL}{path}'
    with urlopen(url) as response:
        payload = response.read()
        obj = json.loads(payload)
        return obj
