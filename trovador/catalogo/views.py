from django.shortcuts import render, get_object_or_404
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
        
        # ordenar categorias a traves de una @property: https://stackoverflow.com/questions/42476581/how-do-i-sort-the-queryset-by-a-propertys-property-django
        'categorias_destacadas': sorted(Categoria.objects.filter(destacado=True), key = lambda x: -(x.productos_count)) 
        # intentos fallidos de ordenar: order by solo funciona con valores almacenados en sql
        # .annotate(num_productos='categoria_productos_count'), #.order_by('num_productos')#order_by('-productos_count')  #
    }
    return render(request, 'productos.html', context)

def producto_detail(request, slug):
    producto = get_object_or_404(Producto, meta_titulo=slug)
    return render(request, 'detalles/detalles_producto.html', context={'producto': producto})

def categoria_detail(request, slug):
    categoria = get_object_or_404(Categoria, meta_titulo=slug)
    categorias_hijas = Categoria.objects.filter(categoria_padre=categoria)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'detalles/detalles_categoria.html', context={
        'categoria': categoria, 
        'categorias_hijas':categorias_hijas,
        'productos':productos
        })

def contacto(request):
    return render(request, 'contacto.html')

def sobrenosotros(request):
    return render(request, 'sobre-nosotros.html')