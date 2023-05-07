from django.conf import settings
from catalogo.models import Producto
from django.forms.models import model_to_dict

class Carrito(object):
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get(settings.CARRITO_SESSION_ID)
        
        if not carrito:
            carrito = self.session[settings.CARRITO_SESSION_ID] = {}
            
        self.carrito = carrito
        
    def __iter__(self):
        for p in self.carrito.keys():
            producto = Producto.objects.get(pk=p)
            self.carrito[str(p)]['producto'] = model_to_dict(producto)
            self.carrito[str(p)]['producto']['imagen'] = str(producto.imagenes[0])

        for item in self.carrito.values():
            item['precio_total'] = item['producto']['precio'] * item['cantidad']
            
            yield item
            
    def __len__(self):
        return sum(item['cantidad'] for item in self.carrito.values())
    
    def save(self):
        self.session[settings.CARRITO_SESSION_ID] = self.carrito
        self.session.modified = True
        
    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)
        
        if product_id not in self.carrito:
            self.carrito[product_id] = {'cantidad': 1, 'id': product_id}
            
        if update_quantity:
            self.carrito[product_id]['cantidad'] += int(quantity)

            if self.carrito[product_id]['cantidad'] == 0:
                self.remove(product_id)
                
        self.save()
        
    def remove(self, product_id):
        if product_id in self.carrito:
            del self.carrito[product_id]
            self.save()