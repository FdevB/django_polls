from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello_view(request):
    return HttpResponse("this is the FIRST view in this tutorial")
