from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import relax
# Create your views here.


def index(request):
    myrelax = relax.objects.all().values()
    template = loader.get_template('main.html')
    context = {
    'myrelax': myrelax,
  }
    return HttpResponse(template.render(context, request))

def message(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def add(request):
    x = request.POST['user']
    y = request.POST['message']
    message = relax(name=x, message=y)
    message.save()
    return HttpResponseRedirect(reverse('index'))