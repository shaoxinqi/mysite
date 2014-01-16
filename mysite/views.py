#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http    import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from usersystem.models import Person
from django.template import RequestContext

def login(request):
    c=  {}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

@login_required(login_url='/accounts/login')
def loggedin(request):
    return render_to_response('loggedin.html',
            {'full_name':request.user.username})

def invalid_login(request):
    return render_to_response('invalid.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login')

def register_user(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
    args={}
    args.update(csrf(request))
    args['form']=UserCreationForm()
    return render_to_response('register.html',args)

def register_success(request):
    return render_to_response('register_success.html')

@csrf_protect
def add(request):
    if request.method == 'POST':
        userid=request.POST.get('userid','')
        name=request.POST.get('name','')
        user=Person(userid=userid, name=name)
        user.save()
        return HttpResponseRedirect('/accounts/add_success')
    return render_to_response('add.html',
                                context_instance=RequestContext(request)
                                )

def add_success(request):
    return render_to_response('add_success.html')

@csrf_protect
def query(request):
    if request.method == 'POST':
	userid=request.POST.get('userid','')
	try:
		res=Person.objects.filter(userid=userid)
	except IndexError:
		return HttpResponse('无法查到该员工编号！')
    return render_to_response('query.html',
				context_instance=RequestContext(request)
				)

def result(request):
    pass

