from django.urls import path
from .  import views

urlpatterns = [
    path('create/',  views.create, name='accounts_create'),
    path('login/',  views.login, name='accounts_login'),
    path('',  views.dashboard, name='accounts_dashboard'),
    path('logout', views.logout, name='accounts_logout')
    ]