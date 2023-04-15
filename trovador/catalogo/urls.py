from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #re_path(r'^productos/?$', views.productos, name='productos'),
    path('productos/', views.productos, name='productos'),
    path('producto/<slug:slug>/', views.producto_detail, name='producto'),
    path('categoria/<slug:slug>/', views.categoria_detail, name='categoria'),
    path('contacto/', views.contacto, name='contacto'),
    path('sobre-nosotros/', views.sobrenosotros, name='sobre-nosotros'),
] 

