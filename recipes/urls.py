from django.urls import path
from . import views

# Request = Cliente faz
# Response = Servidor responde

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'), #Home
    path('recipes/<int:id>/', views.recipe, name='recipe'), #Recipe
   
]