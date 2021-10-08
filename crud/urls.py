from django.urls import path

from . import views


urlpatterns = [
    path('receita/',views.ReceitaView.as_view(), name='crud_receita'),
    path('despesa/',views.despesa, name='crud_despesa'),
    path('emprestimo/',views.emprestimo, name='crud_emprestimo'),
]