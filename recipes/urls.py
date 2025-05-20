from django.urls import path
from recipes.views import home, sobre, contato

# Request = Cliente faz
# Response = Servidor responde

urlpatterns = [
    path('', home), #Home
    path('sobre/',sobre), #/sobre/
    path('contato/', contato), #/contato/
]