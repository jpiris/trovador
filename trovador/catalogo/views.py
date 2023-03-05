from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Función vista para la pagina de inicio del sitio
    """
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')