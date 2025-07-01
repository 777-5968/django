from    django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello,world")
def safari(request):
    return HttpResponse("Hello,safari")
def home(request):
    return render (request,'home.html')

