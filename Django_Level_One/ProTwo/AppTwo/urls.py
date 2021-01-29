from django.urls import path
from AppTwo import views

urlpatterns = [
    path(r'forms/index.html', views.index, name='index'),
    path(r'help/', views.help, name='help'),
    path(r'users/', views.users, name='users'),
    path(r'forms/', views.forms_page, name='forms_page')
]
