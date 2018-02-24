from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm 
from django.template.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt,csrf_protect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('complete/')	
		else:
			form = UserCreationForm()
			token = {}
			token.update(csrf(request))
			token['form'] = form
			return render_to_response('registration/registration_form.html', token)
	
	else:
		form = UserCreationForm()
		token = {}
		token.update(csrf(request))
		token['form'] = form
		return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
	return render_to_response('registration/registration_complete.html')

def base(request):
	return render_to_response('base.html')

@csrf_exempt
def loggedin(request):
	if request.method == 'POST':
		auth = authenticate(username=request.POST['email'] ,password=request.POST['password'])
		if auth is not None:
			login(request, auth)
			return HttpResponseRedirect("/wallet/", {'login': request.POST['email']})
		else:	
			return HttpResponseRedirect('/login/')
	else:
		return HttpResponseRedirect('/login/')	
	

@login_required
def wallet(request):
	return render_to_response('wallet.html')
