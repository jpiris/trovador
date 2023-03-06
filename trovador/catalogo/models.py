from tkinter import image_names
from tokenize import blank_re
from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre de la categoria")
    descripcion_corta = models.TextField(max_length=200, blank=True, help_text="Descripcion corta (max 200 caracteres)")
    #Descripcion larga deberia ser HTML: https://pypi.org/project/django-tinymce/
    descripcion_larga = models.TextField(max_length=1000, blank=True, help_text="Descripcion larga")
    meta_titulo = models.SlugField(null=False, unique=True)
    destacado = models.BooleanField(help_text="Destacado, aparece en la pagina principal")

    imagen1 = models.ImageField(upload_to='uploads/', blank=True)
    fecha_creacion = models.DateField(auto_now_add=True, help_text="Fecha de creación del producto")

    categoria_padre = models.ForeignKey('self', null=True, blank=True, related_name='categoria', on_delete=models.SET_NULL)

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
    precio = models.FloatField(help_text="Precio del producto")
    activo = models.BooleanField(help_text="Activo, aparece en catalogo")
    destacado = models.BooleanField(help_text="Destacado, aparece en la pagina principal")
    stock = models.IntegerField(help_text="Unidades en stock")
    fecha_creacion = models.DateField(auto_now_add=True, help_text="Fecha de creación del producto")
    imagen1 = models.ImageField(upload_to='uploads/')
    imagen2 = models.ImageField(upload_to='uploads/', blank=True)
    imagen3 = models.ImageField(upload_to='uploads/', blank=True)

    meta_titulo = models.SlugField(null=False, unique=True)

    categoria = models.ManyToManyField(Categoria, related_name='cat')

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

