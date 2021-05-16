from django.urls import path, include
from .views import HomepagePainelMaster
from protocolo import urls as protocol_urls
from funcionario import urls as funcionario_urls
from setor import urls as setor_urls


urlpatterns = [
    path('', HomepagePainelMaster.as_view(), name='painel_home'),
    path('protocolo_config/', include(protocol_urls)),
    path('funcionario_config/', include(funcionario_urls)),
    path('setor_config/', include(setor_urls)),

]
