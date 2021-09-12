# Generated by Django 3.2.6 on 2021-09-11 23:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0002_alter_producto_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='fecha')),
                ('cantidad', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='cantidad')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Precio')),
                ('tipoDeOperacion', models.CharField(choices=[('Compra', 'Compra'), ('Venta', 'Venta')], max_length=50, verbose_name='Categoria')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaccion', to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaccion', to='productos.producto', verbose_name='transaccion')),
            ],
            options={
                'verbose_name': 'transacción',
                'verbose_name_plural': 'transacciones',
                'ordering': ['fecha'],
            },
        ),
    ]