from django.urls import path, include
from .views import homepage
from painel import urls as painel_urls
urlpatterns = [
    path('', homepage, name='homepage'),
    path('painel', include(painel_urls)),
]
