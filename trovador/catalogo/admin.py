from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from catalogo.models import Producto, Categoria, User

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion_corta", "productos_count", "destacado")
    prepopulated_fields = {"meta_titulo": ("nombre",)}

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "destacado", "activo")
    prepopulated_fields = {"meta_titulo": ("nombre",)}

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(User, UserAdmin)