from tkinter import image_names
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


    class Meta:
        ordering = ["-fecha_creacion"]

    # Métodos
    def get_absolute_url(self):
         """
         Devuelve la url para acceder a una instancia particular de MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.nombre
