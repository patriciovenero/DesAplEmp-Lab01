from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sumar/<int:n1>/<int:n2>', views.sumar, name='sumar'),
    path('restar/<int:n1>/<int:n2>', views.restar, name='restar'),
    path('multiplicar/<int:n1>/<int:n2>', views.multiplicar, name='multiplicar'),
]