from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name='index'),
    path('plato/<int:plato_id>/',views.plato,name='plato'),
    path('category/<int:cats>/', views.CategoryView, name='category'),
    path('carrito',views.carrito,name='carrito'),
    path('eliminarProductoCarrito/<int:plato_id>',views.eliminarProductoCarrito,name="eliminarProductoCarrito"),
    path('limpiarCarrito',views.limpiarCarrito,name='limpiarCarrito'),
    path('agregarCarrito/<int:plato_id>',views.agregarCarrito,name='agregarCarrito'),
]