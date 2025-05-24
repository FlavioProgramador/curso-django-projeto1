from django.urls import path
from recipes.views import home

# Request = Cliente faz
# Response = Servidor responde

urlpatterns = [
    path('', home), #Home
   
]