import datetime
import json
import os.path
from time import sleep

import requests


def save_file(path):
    if(os.path.exists(path + "log.lock")): # Файл-заглушка, который говорит другим инстансам, что файл занят
        pass
    else:
        try:
            with open(path + "log.lock", 'a+'):
                if (path == './'):
                    filepath = "log"
                else:
                    filepath = path + "log"
                log_to_file(filepath)
        except Exception as e:
            print(e)
        finally:
            if(os.path.exists(path + "log.lock")):
                os.remove(path + "log.lock")

def log_to_file(path):
    last_line = None
    if os.path.exists(path):
        with open(path, 'r') as file:
            lines = file.readlines()
            if len(lines) > 0:
                last_line = lines[-1]
    with open(path, 'a+') as file: # если файл есть, пишем в него, если нет, создаем
        if last_line is None: # если нет никакой предыдущей информации или файл вообще не создан, получаем все строки
            data = get_data()
        else:
            last = last_line.split(' ')[0]
            data = get_data_after_datetime(last)  # иначе смотрим, когда была добавлена последняя запись, и получаем от сервера только те, которые были после нее
        for elem in data:
            file.write(' '.join((elem['created'], str(elem['id']), elem['ip'], elem['method'], elem['uri'], str(elem['statuscode']), '\n')))


def get_data():
    data = requests.get(url = "http://web:8001/api/data/")
    print(data.status_code)
    return data.json()

def get_data_after_datetime(created):
    data = requests.get(url = "http://web:8001/api/data/" , params={'created':created})
    print(data.status_code)
    return data.json()


while True:
    save_file('./logs/')
    sleep(10)