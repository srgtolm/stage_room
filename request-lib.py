__author__ = 'sereg'

import requests

r = requests.get('https://api.github.com/events', auth=('user','pass'))

print r.status_code

