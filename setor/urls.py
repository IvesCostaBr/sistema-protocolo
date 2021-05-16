from django.urls import path
from .views import SetorConfigHome, CriarSetor, DeleteSetor, ListarSetores, EditarSetor


urlpatterns = [
    path('', SetorConfigHome.as_view(), name='setor_home'),
    path('edit_setor/<int:pk>/', EditarSetor.as_view(), name='edit_setor'),
    path('create_setor/', CriarSetor.as_view(), name='create_setor'),
    path('delete_setor/<int:pk>/', DeleteSetor.as_view(), name='delete_setor'),
    path('list_setor/', ListarSetores.as_view(), name='list_setor'),
]
