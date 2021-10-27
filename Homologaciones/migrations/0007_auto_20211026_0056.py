# Generated by Django 3.2.8 on 2021-10-26 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fabricantes', '0002_fabricante_pais_pais'),
        ('Users', '0003_alter_profile_country'),
        ('Homologaciones', '0006_auto_20211026_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencia',
            name='pais',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Fabricantes.pais'),
        ),
        migrations.DeleteModel(
            name='pais',
        ),
    ]