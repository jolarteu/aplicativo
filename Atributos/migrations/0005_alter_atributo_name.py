# Generated by Django 3.2.8 on 2021-10-28 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atributos', '0004_auto_20211028_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atributo',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]