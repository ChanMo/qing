from django.shortcuts import render
from django.http import HttpResponse
from .models import MessageForm
#from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response
from page.models import Site

# Create your views here.
def index(request):
    post = request.POST
    site = Site.objects.get(id=post['site'])
    post.site = site
    message = MessageForm(post)
    if message.is_valid():
        message.save()
        return HttpResponse('success')
    else:
        return HttpResponse(message.errors.as_json())
