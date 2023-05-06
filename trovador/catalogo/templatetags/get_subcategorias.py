from django import template
from catalogo.models import Categoria

register = template.Library()

@register.filter
def get_subcategorias(resultado, categoria):
    return Categoria.objects.filter(categoria_padre=categoria)