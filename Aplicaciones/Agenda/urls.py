#configurando redireccionanmiento
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('dashboard/',views.dashboard, name='dashboard'),
    #URL PROVEEDORES
    path('listadoProveedores/', views.listadoProveedores, name='listadoProveedores'),
    path('eliminarProveedor/<id>', views.eliminarProveedor, name='eliminarProveedor'),
    path('nuevoProveedor/', views.nuevoProveedor, name='nuevoProveedor'),
    path('guardarProveedor/', views.guardarProveedor, name='guardarProveedor'),
    path('editarProveedor/<id>', views.editarProveedor, name='editarProveedor'),
    path('procesarActualizacionProveedor/', views.procesarActualizacionProveedor, name='procesarActualizacionProveedor'),
    #-----------------------------------------PRODUCTOS--------------------------------------------------
   #-----------------------------------------PRODUCTOS--------------------------------------------------
    path('listadoProductos/', views.listadoProductos, name='listadoProductos'),
    path('eliminarProducto/<id>', views.eliminarProducto, name='eliminarProducto'),
    path('nuevoProducto/', views.nuevoProducto, name='nuevoProducto'),
    path('guardarProducto/', views.guardarProducto, name='guardarProducto'),
    path('editarProducto/<id>', views.editarProducto, name='editarProducto'),
    path('procesarActualizacionProducto/', views.procesarActualizacionProducto, name='procesarActualizacionProducto'),

]