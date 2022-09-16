# Generated by Django 4.0.6 on 2022-09-10 03:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAvisoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default=0, max_length=50, unique=True, verbose_name='Mensaje')),
                ('is_active', models.BooleanField(default=True)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Tipo_aviso',
                'verbose_name_plural': 'Tipo_avisos',
                'ordering': ('fecha',),
            },
        ),
    ]
