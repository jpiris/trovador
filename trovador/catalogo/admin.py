from django.contrib import admin
from catalogo.models import Producto, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion_corta", "destacado")
    prepopulated_fields = {"meta_titulo": ("nombre",)}

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "destacado", "activo")
    prepopulated_fields = {"meta_titulo": ("nombre",)}

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)