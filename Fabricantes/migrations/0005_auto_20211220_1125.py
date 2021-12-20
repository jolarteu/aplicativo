# Generated by Django 3.2.8 on 2021-12-20 16:25

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Fabricantes', '0004_auto_20211220_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabricante',
            name='capital',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fabricante_pais',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='fabricante_pais',
            name='numero',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='fabricante_pais',
            name='representante',
            field=models.CharField(max_length=200, null=True),
        ),
    ]