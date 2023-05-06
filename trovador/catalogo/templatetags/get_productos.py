from django import template
from catalogo.models import Producto

register = template.Library()

@register.filter
def get_productos(productos_categoria, categoria):
    return Producto.objects.filter(categoria=categoria)