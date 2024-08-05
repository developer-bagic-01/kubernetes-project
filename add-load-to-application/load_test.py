import requests
import time

url = 'http://134.209.157.252:31239/'

while True:
    try:
        response = requests.get(url)
        print(response.status_code)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    time.sleep(1)

