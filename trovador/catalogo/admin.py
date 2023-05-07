from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from catalogo.models import Producto, ImagenProducto, Categoria, User

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "titulo", "productos_count", "destacado")
    prepopulated_fields = {"meta_titulo": ("nombre",)}
    
class ImagenProductoAdmin(admin.StackedInline):
    model = ImagenProducto
    min_num = 1
    extra = 0
    
class ProductoAdmin(admin.ModelAdmin):    
    list_display = ("nombre", "precio", "destacado", "activo")
    prepopulated_fields = {"meta_titulo": ("nombre",)}
    
    inlines = [ImagenProductoAdmin]

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(User, UserAdmin)