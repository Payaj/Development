# Generated by Django 3.0.6 on 2020-05-26 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0002_address_property_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'address'},
        ),
        migrations.AlterModelOptions(
            name='property_type',
            options={'verbose_name_plural': 'property_type'},
        ),
        migrations.AlterModelOptions(
            name='signup',
            options={'verbose_name_plural': 'signup'},
        ),
    ]
