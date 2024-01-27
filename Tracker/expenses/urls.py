from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/', views.reports, name='reports'),
    path('expenses/', views.expenses, name='expenses'),
]
