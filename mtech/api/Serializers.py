from django.core.serializers.json import DjangoJSONEncoder

from .models import ResponseBody


class RequestBodyEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, ResponseBody):
            return {"id":o.id,
                    "created":o.created,
                    "log":{
                        "ip":o.ip,
                        "method":o.method,
                        "uri":o.uri,
                        "statuscode":o.statuscode
                    }
                    }