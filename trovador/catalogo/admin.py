from django.contrib import admin
from catalogo.models import Producto, Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion_corta")
    prepopulated_fields = {"meta_titulo": ("nombre",)}

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre")
    prepopulated_fields = {"meta_titulo": ("nombre",)}

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria, CategoriaAdmin)