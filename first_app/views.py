from    django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hello world")
def home(request):
    return render (request,'home.html')
def about(request):
    return render(request,'about us.html')
def contact(request):
    return render(request,'contact.html')
