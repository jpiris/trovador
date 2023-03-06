from tkinter import image_names
from tokenize import blank_re
from django.db import models
from django.urls import reverse

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre del producto")
    precio = models.FloatField(help_text="Precio del producto")
    activo = models.BooleanField(help_text="Activo, aparece en catalogo")
    stock = models.IntegerField(help_text="Unidades en stock")
    fecha_creacion = models.DateField(auto_now_add=True, help_text="Fecha de creación del producto")
    imagen1 = models.ImageField(upload_to='uploads/')
    imagen2 = models.ImageField(upload_to='uploads/', blank=True)
    imagen3 = models.ImageField(upload_to='uploads/', blank=True)


    class Meta:
        ordering = ["-fecha_creacion"]

    # Métodos
    def get_absolute_url(self):
         """
         Devuelve la url para acceder a una instancia particular de MyModelName.
         """
         return reverse('producto', args=[str(self.id)])

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, help_text="Nombre de la categoria")
    descripcion_corta = models.TextField(max_length=200, help_text="Descripcion corta (max 200 caracteres)")
    #Descripcion larga deberia ser HTML: https://pypi.org/project/django-tinymce/
    descripcion_larga = models.TextField(max_length=1000, help_text="Descripcion larga")
    meta_titulo = models.SlugField(null=False, unique=True)

    fecha_creacion = models.DateField(auto_now_add=True, help_text="Fecha de creación del producto")

    categoria_padre = models.ForeignKey('self', null=True, related_name='categoria', on_delete=models.SET_NULL)