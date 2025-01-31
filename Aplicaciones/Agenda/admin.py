from django.contrib import admin

# Register your models here.
from.models import Producto, Proveedor

admin.site.register(Producto)
admin.site.register(Proveedor)