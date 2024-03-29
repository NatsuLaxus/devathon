from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate, login

from .forms import UserRegistrationForm, UserLoginForm

def index(request):
	user = request.user
	data = {}
	data['user'] = user
	data['isAdmin'] = user.is_superuser
	return render(request, 'index.html', data)

def login_page(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			password = userObj['password']
			user = authenticate(username = username, password = password)
			if user is not None:
				login(request,user)
				return redirect('/home')
		else:
			raise forms.ValidationError('wrong!')
	else:
		form = UserLoginForm()
	return render(request, 'login.html', {'form':form})

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			email =  userObj['email']
			password =  userObj['password']
			firstname =  userObj['first_name']
			lastname =  userObj['last_name']
			contact = userObj['contact']

			if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
				user = User.objects.create_user(username = username ,email= email)
				user.set_password(password)
				user.first_name = firstname
				user.last_name = lastname
				user.save()
				login(request,user)
				
				return redirect('/')
			else:
				return render(request, 'registration.html',{'error': 'This Username/Email is not available!', 'form' : form})

	else:
	 	form = UserRegistrationForm()

	return render(request, 'registration.html', {'form' : form})

def home(request):
	user = request.user
	data = {}
	data['user'] = user
	return render(request,'home2.html',data)

@login_required(login_url='login/')
def logout_page(request):
    logout(request)
    return redirect('/login')

