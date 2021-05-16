from django.urls import path
from .views import SetorConfigHome


urlpatterns = [
    path('', SetorConfigHome.as_view(), name='setor_home'),
]
