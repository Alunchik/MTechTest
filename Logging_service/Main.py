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
            with open(path + "log.lock", 'w+'):
                if (path == './'):
                    filepath = "log"
                else:
                    filepath = path + "log"
                log_to_file(filepath)
        except Exception as e:
            print(e)
        finally:
            os.remove(path + "log.lock")

def log_to_file(path):
    last_line = None

    if os.path.exists(path):
        with open(path, 'r') as file:
            lines = file.readlines()
            if len(lines)>0:
                last_line = file.readlines()[-1]
    with open(path, 'w+') as file: # если файл есть, пишем в него, если нет, создаем
        if last_line is None: # если нет никакой предыдущей информации или файл вообще не создан, получаем все строки
            data = get_data()
        else:
            last = last_line.split(' ')[0]
            data = get_data_after_datetime(last)  # иначе смотрим, когда была добавлена последняя запись, и получаем от сервера только те, которые были после нее
            print(data)
        print(data)
        for elem in data:
            file.write(' '.join((elem['created'], str(elem['id']), elem['ip'], elem['method'], elem['uri'], str(elem['statuscode']), '\n')))


def get_data():
    data = requests.get(url = "http://127.0.0.1:8000/api/data/")
    return data.json()

def get_data_after_datetime(created):
    data = requests.get(url = "http://127.0.0.1:8000/api/data/" , params={'created':created})
    return data.json()


while True:
    save_file('./')
    sleep(10)