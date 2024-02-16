from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("Hello Worldddddd")

def homepage(request):
    return HttpResponse("Heyyyy")

def click(request):
    return render(request,'index.html')