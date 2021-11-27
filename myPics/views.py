from django.shortcuts import render,redirect

from django.http  import HttpResponse,Http404
import datetime as dt
from . models import Image, Location, Category

# Create your views here.

def welcome(request):
    title = 'Welcome to A++ Gallery'
    images = Image.objects.all()
    context={
        'title': title,
        'images' : images,
    }
    return render(request, 'welcome.html', context)