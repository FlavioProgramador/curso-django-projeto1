from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', status=201, context={
        'name': 'Flavio Costa',
        'age':21,
    })

def contato(request):
    return HttpResponse("Contato 1")

def sobre(request):
    return HttpResponse("Sobre 1")
