from django.shortcuts import get_object_or_404,render
from .models import Plato,Categoria
from .carrito import Cart
# Create your views here.
def index(request):
    product_list = Plato.objects.all
    categories = Categoria.objects.all
    context = {
        'platos': product_list,
        'categories': categories
        }
    return render(request,'index.html',context)

def plato(request,plato_id):
    plato = get_object_or_404(Plato,pk=plato_id)
    return render(request,'detalle.html',{'plato':plato})

def CategoryView(request, cats):
    food_list = Plato.objects.filter(categoria=cats)
    return render(request, 'index.html', { 'platos':food_list})

def agregarCarrito(request,plato_id):
    objPlato = Plato.objects.get(id=plato_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objPlato,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,plato_id):
    objPlato = Plato.objects.get(id=plato_id)
    carritoPlato = Cart(request)
    carritoPlato.remove(objPlato)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoPlato = Cart(request)
    CarritoPlato.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')