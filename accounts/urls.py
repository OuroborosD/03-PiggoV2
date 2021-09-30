from django.urls import path
from .import views

urlpatterns= [
    path('create/', views.create, name='accounts_create'),
    path('login/', views.login, name='accounts_login'),
    path('logout/', views.logout, name='accounts_logout'),
    path('dashboard/', views.dashboard, name='accounts_dashboard')
    ]