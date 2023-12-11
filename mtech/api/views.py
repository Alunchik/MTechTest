import json
from datetime import datetime

from asgiref.sync import sync_to_async, async_to_sync
from django.contrib.postgres import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from . import utils
from .models import ResponseBody


# Create your views here.

@sync_to_async()
def upload_data(request):
    if request.method=='POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        request_str_list = utils.getResponseBody(data['str'])
        ResponseBody.objects.create(created=datetime.now(), ip=request_str_list[0],
    method=request_str_list[1], uri=request_str_list[2], statuscode=request_str_list[3]) #сохраняем объект в базу данных
        return HttpResponse(status=200)
@sync_to_async()
def get_data(request):
    if request.GET.get('method'):
        return get_data_by_method(request.GET.get('method'))
    if request.GET.get('created'):
        return get_data_after_datetime(request.GET.get('created'))
    return get_all()


def get_data_after_datetime(cerated):  # записи добавленные после определенного времени
    obj = ResponseBody.objects.filter(created__gt=cerated).values()
    return JsonResponse(list(obj), status=200, safe=False)

def get_data_by_method(method):
    obj = ResponseBody.objects.filter(method=method).values()
    return JsonResponse(list(obj), status=200, safe=False)

def get_all():
    obj = ResponseBody.objects.all().values()
    return JsonResponse(list(obj), status=200, safe=False)

@csrf_exempt
async def data(request):
    if request.method == 'POST':
        return await upload_data(request)
    else:
        return await get_data(request)