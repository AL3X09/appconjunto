# Generated by Django 4.0.6 on 2022-09-10 03:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditoriaPedidoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarios', models.CharField(max_length=255, unique=True, verbose_name='Detalles')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('is_esperapedido', models.BooleanField(default=True, verbose_name='Se Espera Pedido')),
                ('is_entregado', models.BooleanField(default=False, verbose_name='Pedido Entregado')),
                ('code', models.CharField(default='code', max_length=500, unique=True, verbose_name='Código')),
                ('is_validcode', models.BooleanField(default=False, verbose_name='Código Valido')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'AuditoriaPedido',
                'verbose_name_plural': 'AuditoriaPedidos',
            },
        ),
    ]
