from tkinter import image_names
from tokenize import blank_re
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    pass

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre de la categoria")
    titulo = models.TextField(max_length=200, blank=True, help_text="Titulo de la pàgina del catalogo")
    #Descripcion larga deberia ser HTML: https://pypi.org/project/django-tinymce/
    descripcion = models.TextField(max_length=1000, blank=True, help_text="Descripcion larga")
    meta_titulo = models.SlugField(null=False, unique=True)
    destacado = models.BooleanField(help_text="Destacado, aparece en la pagina principal")

    imagen = models.ImageField(upload_to='uploads/', blank=True)
    categoria_padre = models.ForeignKey('self', null=True, blank=True, related_name='categoria', on_delete=models.SET_NULL)
    
    fecha_creacion = models.DateField(auto_now_add=True, help_text="Fecha de creación de la categoria")
    fecha_modificacion = models.DateField(auto_now=True, help_text="Fecha de modificación de la categoria")

    # Propiedades
    @property
    def productos_count(self):
        return Producto.objects.filter(categoria=self).count()

    # Métodos
    def get_absolute_url(self):
         """
         Devuelve la url para acceder a una Categoria
         """
         return reverse('categoria', args=[str(self.meta_titulo)])

    def __str__(self):
        """
        Cadena para representar el objeto (en el sitio de Admin, etc.)
        """
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre del producto")
    referencia = models.CharField(max_length=20, help_text="Referencia del producto")
    precio = models.FloatField(help_text="Precio del producto")
    activo = models.BooleanField(help_text="Activo, aparece en catalogo")
    destacado = models.BooleanField(help_text="Destacado, aparece en la pagina principal")
    stock = models.IntegerField(help_text="Unidades en stock")
    porcentajeDescuento = models.IntegerField(default=0, help_text="Porcentaje de descuento", validators=[
        MaxValueValidator(100),
        MinValueValidator(0),
    ])
    
    meta_titulo = models.SlugField(null=False, unique=True)

    categoria = models.ForeignKey(Categoria, default=None, null=True, on_delete=models.SET_NULL)
    
    fecha_creacion = models.DateField(auto_now_add=True, help_text="Fecha de creación")
    fecha_modificacion = models.DateField(auto_now=True, help_text="Fecha de modificación")

    # Propiedades
    @property
    def imagenes(self):
        return ImagenProducto.objects.filter(producto=self)

    class Meta:
        ordering = ["-fecha_creacion"]

    # Métodos
    def get_absolute_url(self):
         """
         Devuelve la url para acceder a una instancia particular de Producto.
         """
         return reverse('producto', args=[str(self.meta_titulo)])

    def __str__(self):
        """
        Cadena para representar el objeto Producto (en el sitio de Admin, etc.)
        """
        return self.nombre
    
class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, default=None, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='uploads/')
    
    fecha_creacion = models.DateField(auto_now_add=True, help_text="Fecha de creación de la categoria")
    fecha_modificacion = models.DateField(auto_now=True, help_text="Fecha de modificación de la categoria")
    
    def __str__(self):
        return self.imagen.url


