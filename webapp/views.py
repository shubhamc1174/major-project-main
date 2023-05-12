from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def home(request):
#     return HttpResponse("hello")
	return render(request, 'dashboard.html')

def about(request):
	return render(request, 'about.html')


def pkgs(request):
	return render(request, 'pkgs.html')

def dashboard(request):
	return render(request, 'dashboard.html')

