# Generated by Django 4.0.6 on 2022-09-10 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoParqueaderoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True, verbose_name='Detalles')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'TipoParqueadero',
                'verbose_name_plural': 'TipoParqueaderos',
            },
        ),
    ]
