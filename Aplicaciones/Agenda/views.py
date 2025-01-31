from django.shortcuts import render, redirect, get_object_or_404
from .models import Proveedor, Producto
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Para los dashboard
from django.db.models import Count

# Home
def home(request):
    return render(request,"home.html")

def dashboard(request):
    # Consulta que cuenta el número de proveedores por estado
    proveedores = Proveedor.objects.values('estado_prove').annotate(count=Count('id_prove'))

    # Consulta que cuenta el número de productos por tipo
    productos = Producto.objects.values('tipo_prod').annotate(count=Count('id_prod'))

    # Consulta para obtener los productos con stock menor a 5, ordenados ascendentemente
    productos_bajos_stock = Producto.objects.filter(stock_prod__lt=5).order_by('stock_prod')[:3]

    # Pasar ambos conjuntos de datos al contexto
    return render(request, 'dashboard.html', {
        'proveedores': proveedores,
        'productos': productos,
        'productos_bajos_stock': productos_bajos_stock
    })

#----------------------------------------PROVEEDORES
# Listar Proveedores
def listadoProveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "listadoProveedores.html", {'proveedores': proveedores})

# Eliminar Proveedor
def eliminarProveedor(request, id):
    proveedorEliminar = Proveedor.objects.get(id_prove=id)
    proveedorEliminar.delete()
    messages.success(request, "Proveedor eliminado exitosamente.")
    return redirect('listadoProveedores')

# Formulario Nuevo Proveedor
def nuevoProveedor(request):
    return render(request, 'nuevoProveedor.html')

# Guardar Nuevo Proveedor
def guardarProveedor(request):
    ruc = request.POST["ruc_prove"]
    nombre = request.POST["nombre_prove"]
    telefono = request.POST["telefono_prove"]
    estado = request.POST["estado_prove"]
    Proveedor.objects.create(ruc_prove=ruc, nombre_prove=nombre, telefono_prove=telefono, estado_prove=estado)
    messages.success(request, "Proveedor registrado exitosamente.")
    return redirect('listadoProveedores')

# Formulario Editar Proveedor
def editarProveedor(request, id):
    proveedorEditar = Proveedor.objects.get(id_prove=id)
    return render(request, 'editarProveedor.html', {'proveedorEditar': proveedorEditar})

# Actualizar Proveedor
def procesarActualizacionProveedor(request):
    id = request.POST['id_prove']
    ruc = request.POST['ruc_prove']
    nombre = request.POST['nombre_prove']
    telefono = request.POST['telefono_prove']
    estado = request.POST['estado_prove']
    proveedorConsultado = Proveedor.objects.get(id_prove=id)
    proveedorConsultado.ruc_prove = ruc
    proveedorConsultado.nombre_prove = nombre
    proveedorConsultado.telefono_prove = telefono
    proveedorConsultado.estado_prove = estado
    proveedorConsultado.save()
    messages.success(request, "Proveedor actualizado exitosamente.")
    return redirect('listadoProveedores')

#----------------------------------------PRODUCTOS
# Listado de Productos
def listadoProductos(request):
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    return render(request, "listadoProductos.html", {'productos': productos, 'proveedores': proveedores})

# Eliminar Producto
def eliminarProducto(request, id):
    productoEliminar = Producto.objects.get(id_prod=id)
    productoEliminar.delete()
    messages.success(request, "Producto eliminado exitosamente.")
    return redirect('listadoProductos')

# Formulario Nuevo Producto
def nuevoProducto(request):
    proveedores = Proveedor.objects.all()  # Obtener todos los proveedores
    return render(request, 'nuevoProducto.html', {'proveedores': proveedores})

# Guardar Nuevo Producto
def guardarProducto(request):
    nombre = request.POST["nombre_prod"]
    stock = request.POST["stock_prod"]
    precio = request.POST["precio_prod"]
    tipo = request.POST["tipo_prod"]
    fecha = request.POST["fecha_prod"]
    cantidad = request.POST["cantidad_prod"]
    proveedor_id = request.POST["id_prove"]
    proveedor = Proveedor.objects.get(id_prove=proveedor_id)
    Producto.objects.create(
        nombre_prod=nombre,
        stock_prod=stock,
        precio_prod=precio,
        tipo_prod=tipo,
        fecha_prod=fecha,
        cantidad_prod=cantidad,
        id_prove=proveedor
    )
    messages.success(request, "Producto registrado exitosamente.")
    return redirect('listadoProductos')


# Vista para editar producto
def editarProducto(request, id):
    productoEditar = Producto.objects.get(id_prod=id)
    # Convertir el precio a un número con 2 decimales
    precio_formateado = "{:.2f}".format(productoEditar.precio_prod)
    proveedores = Proveedor.objects.all()
    return render(request, 'editarProducto.html', {'productoEditar': productoEditar, 'precio_formateado': precio_formateado, 'proveedores': proveedores})
# Actualizar Producto
# Vista para procesar la actualización de producto
def procesarActualizacionProducto(request):
    id_prod = request.POST['id_prod']
    nombre = request.POST['nombre_prod']
    stock = request.POST['stock_prod']
    precio = request.POST['precio_prod']
    tipo = request.POST['tipo_prod']
    fecha = request.POST['fecha_prod']
    cantidad = request.POST['cantidad_prod']
    id_prove = request.POST['id_prove']

    # Obtener el proveedor correspondiente
    proveedor = Proveedor.objects.get(id_prove=id_prove)
    
    # Actualizar el producto
    producto = Producto.objects.get(id_prod=id_prod)
    producto.nombre_prod = nombre
    producto.stock_prod = stock
    producto.precio_prod = precio
    producto.tipo_prod = tipo
    producto.fecha_prod = fecha
    producto.cantidad_prod = cantidad
    producto.id_prove = proveedor
    producto.save()

    messages.success(request, "Producto actualizado exitosamente.")
    return redirect('listadoProductos')
