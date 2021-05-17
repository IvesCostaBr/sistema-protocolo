from django.urls import path, include
from .views import homepage, RegistrarLogin, Reg
from painel import urls as painel_urls
urlpatterns = [
    path('', homepage, name='homepage'),
    path('painel/', include(painel_urls)),
    path('register/', RegistrarLogin.as_view(), name='register_login'),
    path('a/', Reg.as_view(), name='reg')
]
