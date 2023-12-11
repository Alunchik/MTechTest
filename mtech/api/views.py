import json
from datetime import datetime

from django.contrib.postgres import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from . import utils
from .models import ResponseBody


# Create your views here.

def upload_data(request):
    if request.method=='POST':
        try:
            data = json.loads()
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        request_str_list= utils.getResponseBody(data['str'])
        ResponseBody.objects.create(created=datetime.now(), ip=request_str_list[0],
    method=request_str_list[1], uri=request_str_list[2], statuscode=request_str_list[3]) #сохраняем объект в базу данных
        return HttpResponse(status=200)

def get_data(request):
    if request.GET.get('method'):
        return get_data_by_method(request.GET.get('method'))
    return get_all()

def get_data_by_method(method):
    data = obj = ResponseBody.objects.filter(method=method).values()
    return JsonResponse(list(obj), status=200, safe=False)

def get_all():
    data = obj = ResponseBody.objects.all().values()
    return JsonResponse(list(obj), status=200, safe=False)

@csrf_exempt
def data(request):
    if request.method == 'POST':
        return upload_data(request)
    else:
        return get_data(request)