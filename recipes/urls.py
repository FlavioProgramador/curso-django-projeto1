from django.urls import path
from . import views

# Request = Cliente faz
# Response = Servidor responde

urlpatterns = [
    path('', views.home), #Home
    path('recipes/<int:id>/', views.recipe), #Recipe
   
]