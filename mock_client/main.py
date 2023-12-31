import json
import random
import sys
import threading
from datetime import time
from time import sleep
import requests
from concurrent.futures import Executor, ThreadPoolExecutor


def generate_string():
    ipaddress = '192.186.10.35'
    method_list = ['GET', 'POST', 'PUT', 'DELETE']
    HTTP_method = random.choice(method_list)
    uri = 'https://www.google.com/search?q=google'
    HTTP_status = random.randint(100, 599)
    string = ' '.join((ipaddress, HTTP_method, uri, str(HTTP_status)))
    return string

def post(delay):
    while True:
        string = generate_string()
        data = {"str": string}
        try:
            resp = requests.post(url="http://web:8001/api/data/", data=json.dumps(data))
            print(resp.status_code)
        except Exception as e:
            print(e)
        # print(string + "sent")

        sleep(delay)


delay = int(sys.argv[1])
counter = int(sys.argv[2])

#with ThreadPoolExecutor(max_workers=counter) as executor:
#    executor.map(post, [delay for i in range(counter)])
for i in range(counter):
    threading.Thread(target=post, args=(delay,)).start()
