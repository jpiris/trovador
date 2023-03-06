from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('producto/<slug:slug>/', views.producto_detail, name='producto'),
    path('categoria/<slug:slug>/', views.categoria_detail, name='categoria'),
    path('contacto/', views.contacto, name='contacto'),
    path('sobre-nosotros/', views.sobrenosotros, name='sobre-nosotros'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)