# Generated by Django 3.0.6 on 2020-06-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=10)),
                ('bed', models.IntegerField()),
                ('bath', models.FloatField()),
                ('sqft', models.FloatField()),
                ('price', models.BigIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Property_Info',
            },
        ),
    ]
