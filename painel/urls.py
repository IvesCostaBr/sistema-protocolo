from django.urls import path, include
from .views import (painel_home,
adicionar_func, mostar_funcionarios, remove_funcionario,
edit_funcionarios,

)

urlpatterns = [
    path('', painel_home, name='painel_home'),
    path('gestao/', adicionar_func, name='gestao' ),
    path('mostrar_funcionarios/', mostar_funcionarios, name='funcionario_view'),
    path('deletar_func/<int:id>/',remove_funcionario , name='deletar_func'),
    path('edit_func/<int:id>/', edit_funcionarios, name='edit_fun')

]
