from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def msql(request):
    return HttpResponse('data is added')