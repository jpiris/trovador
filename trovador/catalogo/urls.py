from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('sobre-nosotros/', views.sobrenosotros, name='sobre-nosotros'),
]