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
    path('carrito/', views.carrito, name='carrito'),
    path('add_to_carrito/<int:product_id>', views.add_to_carrito, name='add_to_carrito'),
    path('rebajas/', views.rebajas, name='rebajas'),
    path('busqueda/', views.busqueda, name='busqueda'),
] 

