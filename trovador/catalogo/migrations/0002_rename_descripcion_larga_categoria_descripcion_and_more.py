# Generated by Django 4.2.1 on 2023-05-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalogo", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="categoria",
            old_name="descripcion_larga",
            new_name="descripcion",
        ),
        migrations.RemoveField(
            model_name="categoria",
            name="descripcion_corta",
        ),
        migrations.AddField(
            model_name="categoria",
            name="titulo",
            field=models.TextField(
                blank=True, help_text="Titulo de la pàgina del catalogo", max_length=200
            ),
        ),
    ]
