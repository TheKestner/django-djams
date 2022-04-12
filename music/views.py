from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the music index.")

def results(request):
    data = {}
    songs = Song.objects.all().values()
    data = list(songs) 
    return JsonResponse({"Data":data})