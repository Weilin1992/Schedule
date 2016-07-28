from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

def sign_log(request):
    return render_to_response('account/sign_log.html',RequestContext(request, {}))
