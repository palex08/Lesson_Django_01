from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>My first django project</h1>")

def new(request):
    return HttpResponse("<h1>My second django project</h1>")