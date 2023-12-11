import datetime
from datetime import timezone

from django.db import models

# Create your models here.



class ResponseBody(models.Model):
    created = models.DateTimeField(default=datetime.datetime.now())
    ip = models.GenericIPAddressField(protocol='IPv4')
    method = models.CharField(default="GET")
    uri = models.URLField(default="ya.ru")
    statuscode = models.IntegerField(default=404)

class RequestBody(models.Model):
    str = models.CharField(default='')

