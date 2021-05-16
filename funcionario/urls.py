from django.urls import path
from .views import (
adicionar_func, mostar_funcionarios, remove_funcionario,
edit_funcionarios, FuncionarioConfigHome

)

urlpatterns = [
    path('', FuncionarioConfigHome.as_view(), name='funcionario_home'),
    path('adicionar_func/', adicionar_func, name='add_func' ),
    path('mostrar_funcionarios/', mostar_funcionarios, name='funcionario_view'),
    path('deletar_func/<int:id>/',remove_funcionario , name='deletar_func'),
    path('edit_func/<int:id>/', edit_funcionarios, name='edit_fun'),


]

