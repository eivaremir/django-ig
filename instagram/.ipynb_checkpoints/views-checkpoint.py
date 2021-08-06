
from django.http import HttpResponse
import pdb
import json 
def hello_world(request):
    pdb.set_trace()
    return HttpResponse(json.dumps({
        'body':[int(x) for x in request.GET['numbers'].split(',')],
        'status':'ok'
    }), content_type='application/json')