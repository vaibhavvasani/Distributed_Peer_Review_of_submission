from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request,'peer/home.html',{'title':'Home'})

def about(request):
	return HttpResponse('<h1>About Page</h1>')