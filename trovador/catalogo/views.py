from django.shortcuts import render

from catalogo.models import Producto

# Create your views here.
def index(request):
    """
    Función vista para la pagina de inicio del sitio
    """
    return render(request, 'index.html')

def productos(request):
    context = {
        'productos_list': Producto.objects.order_by('-id')[:4]
    }
    return render(request, 'productos.html', context)

def contacto(request):
    return render(request, 'contacto.html')

def sobrenosotros(request):
    return render(request, 'sobre-nosotros.html')