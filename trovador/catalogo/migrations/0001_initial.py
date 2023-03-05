# Generated by Django 4.1.7 on 2023-03-04 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del producto', max_length=50)),
                ('precio', models.FloatField(help_text='Precio del producto')),
                ('activo', models.BooleanField(help_text='Activo, aparece en catalogo')),
                ('stock', models.IntegerField(help_text='Unidades en stock')),
                ('fecha_creacion', models.DateField(auto_now_add=True, help_text='Fecha de creación del producto')),
                ('imagen1', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
