from django import urls

from catalogo import views

urlpatterns = [
    urls(r'^$', views.index, name='index'),
]