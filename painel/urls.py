from django.urls import path, include
from .views import (painel_home,
adicionar_func
)

urlpatterns = [
    path('', painel_home, name='painel_home'),
    path('gestao/', adicionar_func, name='gestao' ),
]
