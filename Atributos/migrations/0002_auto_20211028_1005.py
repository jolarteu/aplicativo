# Generated by Django 3.2.8 on 2021-10-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atributos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atributo',
            name='Obligatorio',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='atributo',
            name='status_activo',
            field=models.BooleanField(default=True),
        ),
    ]
