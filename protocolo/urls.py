from django.urls import path
from .views import (
    show_protocol, ProtocoloConfigHome,
    ProtocoloCreate, EditarProtocolo,
    DeleteProtocolo,
    )

urlpatterns = [
    path('list_protocolo/', show_protocol, name='list_protocol'), 
    path('', ProtocoloConfigHome.as_view(), name='protocolo_home'),
    path('protocolo_form/', ProtocoloCreate.as_view(), name='protocolo_form'),
    path('editar_protocolo/<int:pk>/', EditarProtocolo.as_view(), name='editar_protocolo'),
    path('delete_protocolo/<int:pk>/', DeleteProtocolo.as_view(), name='delete_protocolo'),
]
