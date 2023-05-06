# Generated by Django 4.2.1 on 2023-05-06 19:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalogo", "0002_rename_descripcion_larga_categoria_descripcion_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="producto",
            name="porcentajeDescuento",
            field=models.IntegerField(
                default=0,
                help_text="Porcentaje de descuento",
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(0),
                ],
            ),
        ),
    ]
