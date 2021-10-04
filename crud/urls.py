from django.urls import path

from . import views


urlpatterns = [
    path('receita/',views.receita, name='crud_receita'),
    path('despesa/',views.despesa, name='crud_despesa'),
    path('emprestimo/',views.emprestimo, name='crud_emprestimo'),
]