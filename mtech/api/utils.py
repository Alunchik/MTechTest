from datetime import datetime

from .models import ResponseBody


def getResponseBody(request_str):
    # делаем без проверок для упрощения работы в тестовом задании
    # считаем, что данные приходят гарантированно  правильные
    request_str_list = request_str.split(' ')
   # parsed_obj = ResponseBody(created=datetime.now(), ip=request_str_list[0], method=request_str_list[1], uri=request_str_list[2], statuscode=request_str_list[3])
    # parsed_obj = {ResponseBody(}created=datetime.now(), ip=request_str_list[0],
    # method=request_str_list[1], uri=request_str_list[2], statuscode=request_str_list[3])

    return request_str_list