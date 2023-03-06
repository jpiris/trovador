from django.shortcuts import render
from django.db.models import Count
from catalogo.models import Producto, Categoria

# Create your views here.
def index(request):
    """
    Función vista para la pagina de inicio del sitio
    """
    return render(request, 'index.html')

def productos(request):
    context = {
        'productos_list': Producto.objects.filter(activo=True).order_by('-id')[:4],
        'categorias_destacadas': Categoria.objects.filter(destacado=True).annotate(num_productos=Count('producto_set')).order_by('num_productos')
    }
    return render(request, 'productos.html', context)

def contacto(request):
    return render(request, 'contacto.html')

def sobrenosotros(request):
    return render(request, 'sobre-nosotros.html')