# Generated by Django 3.2.8 on 2021-10-26 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fabricantes', '0002_fabricante_pais_pais'),
        ('Users', '0002_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Fabricantes.pais'),
        ),
    ]