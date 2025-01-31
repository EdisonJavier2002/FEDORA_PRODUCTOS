from django.db import models

class Proveedor(models.Model):
    id_prove = models.AutoField(primary_key=True)
    ruc_prove = models.CharField(max_length=13, unique=True)
    nombre_prove = models.CharField(max_length=255)
    telefono_prove = models.CharField(max_length=15)
    estado_prove = models.CharField(max_length=50)

    def __str__(self):
        return f"ID: {self.id_prove}, Nombre: {self.nombre_prove}, RUC: {self.ruc_prove}, Estado: {self.estado_prove}"

class Producto(models.Model):
    id_prod = models.AutoField(primary_key=True)
    nombre_prod = models.CharField(max_length=255)
    stock_prod = models.IntegerField()
    precio_prod = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_prod = models.CharField(max_length=100)
    fecha_prod = models.DateField()
    cantidad_prod = models.IntegerField()
    id_prove = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id_prod}, Nombre: {self.nombre_prod}, Stock: {self.stock_prod}, Precio: {self.precio_prod}"
