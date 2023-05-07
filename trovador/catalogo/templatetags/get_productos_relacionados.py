from django import template
from catalogo.models import Producto
from django.db.models import Q

register = template.Library()

@register.filter
def get_productos_relacionados(productos_relacionados, producto):
    return Producto.objects.filter(Q(categoria=producto.categoria) & ~Q(pk=producto.pk))