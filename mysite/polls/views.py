from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
     return HttpResponse('PARIN MADHAV BORN ON MAY31 2020')