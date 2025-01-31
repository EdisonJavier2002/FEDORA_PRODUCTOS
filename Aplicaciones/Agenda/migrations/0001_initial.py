# Generated by Django 4.0.6 on 2025-01-31 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_prove', models.AutoField(primary_key=True, serialize=False)),
                ('ruc_prove', models.CharField(max_length=13, unique=True)),
                ('nombre_prove', models.CharField(max_length=255)),
                ('telefono_prove', models.CharField(max_length=15)),
                ('estado_prove', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_prod', models.CharField(max_length=255)),
                ('stock_prod', models.IntegerField()),
                ('precio_prod', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo_prod', models.CharField(max_length=100)),
                ('fecha_prod', models.DateField()),
                ('cantidad_prod', models.IntegerField()),
                ('id_prove', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agenda.proveedor')),
            ],
        ),
    ]
