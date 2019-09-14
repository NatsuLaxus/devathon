from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate, login
import datetime
from .models import *
# from .forms import 
# Create your views here.
def check_admin(user):
	return user.is_superuser

def check_student(user):
	return user.is_superuser==0

@login_required(login_url='login/')
@user_passes_test(check_admin)
def index(request):
	vehicles = VehicleType.objects.filter(vehicle_type = 1)
	data = {}
	for v in vehicles:
		r = {}
		r['reg'] = v.vehicle_num
		r['owner'] = v.name
		r['entry'] = v.entry_time
		r['exit'] = v.exit_time
		data['details'].append(r)
	return render(request, 'home.html', data)

@login_required(login_url='login/')
@user_passes_test(check_admin)
def inside(request):
	vehicles = VehicleStatus.objects.filter(status = 1)
	data = {}
	for v in vehicles:
		r = {}
		r['reg'] = v.vehicle_num
		r['owner'] = v.name
		data['details'].append(r)
	return render(request, 'home4.html', data)
