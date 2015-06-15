from django.shortcuts import render
from . import crypt

# Create your views here.
def index(request):
    if crypt.valid():
        pass
    else:
        return HttpResponse("error")

    return HttpResponse("haha")
