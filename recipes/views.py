from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', status=201)

def recipe(request,id):
    return render(request, 'recipes/pages/recipe-view.html', status=201)

