#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
import datetime

#@login_required(login_url='/accounts/login')
def main(request):
	return render_to_response('main.html')

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('main.html')
		else:
			print "disabled account."
	else:
		print "invalid login."
	
def logout(request):
	logout(request)
	return render_to_response('/registration/login.html')
	#return HttpResponseRedirect('/accounts/login')
	
def hello(resquest):
	return HttpResponse('hello, Django!')

