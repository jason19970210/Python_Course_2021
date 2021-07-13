# -*- coding: utf-8 -*-

import requests

target_url = 'https://shopee.tw/'

resp = requests.get(target_url)

print(resp)