from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import relax
from .models import talk
# Create your views here.

def talk(request):
    board = relax.objects.all().values()
    context = {
            'board': board,
            'status':0,
            }
    template = loader.get_template('main2-1.html')
    return HttpResponse(template.render(context))

def talk2(request):
    board = talk.objects.all().values()
    context = {
            'board': board,
            'status':1,
            }
    template = loader.get_template('main2-1.html')
    return HttpResponse(template.render(context))

def member(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))

def regist(request):
    context = {
            'status':0,
            }
    x = request.POST['user']
    y = request.POST['pass']
    z = request.POST['repass']
    if y == z:
        message = relax(user=x, password=y)
        message.save()
        template = loader.get_template('main2-1.html')
        return HttpResponse(template.render(context, request)) 
    else:
        template = loader.get_template('error.html')
        return HttpResponse(template.render({}, request))
    
    
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request)) 


def log(request):
    x = request.POST['user']
    y = request.POST['pass']
    myrelax = relax.objects.filter(user= x).values()
    for x in myrelax:
        mypassword = relax.objects.filter(password= y).values()
        for y in mypassword:
            context = {
            'myrelax': myrelax,
            'status':1,
            'username':x,
            }
            template = loader.get_template('main2-1.html')
            return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template('error2.html')
            return HttpResponse(template.render({}, request))
        
        
    else:
        template = loader.get_template('error2.html')
        return HttpResponse(template.render({}, request))
    
def add(request):
    a = request.POST['user']
    b = request.POST['message']
    comment = talk(user=a, message=b)
    comment.save()
    return HttpResponseRedirect(reverse('talk2'))

        
#def log2(request):
#    x = request.POST['user']
#    y = request.POST['pass']
#    data = relax.objects.all().values()
#    if x in data:
#        myrelax = relax.objects.filter(user= '').values(x)
#        for z in myrelax:
#            if y == z.password:
#                context = {
#                'myrelax': myrelax,
#                }
#                template = loader.get_template('access.html')
#                return HttpResponse(template.render(context, request))
#
#    else:
#        template = loader.get_template('error2.html')
#        return HttpResponse(template.render({}, request))      
        