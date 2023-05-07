# Generated by Django 4.2.1 on 2023-05-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalogo", "0004_categoria_fecha_modificacion_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="producto",
            name="imagen1",
        ),
        migrations.RemoveField(
            model_name="producto",
            name="imagen2",
        ),
        migrations.RemoveField(
            model_name="producto",
            name="imagen3",
        ),
        migrations.AddField(
            model_name="imagenproducto",
            name="imagen",
            field=models.ImageField(default=None, upload_to="uploads/"),
            preserve_default=False,
        ),
    ]