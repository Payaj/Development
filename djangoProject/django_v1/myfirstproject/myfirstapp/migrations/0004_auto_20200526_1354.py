# Generated by Django 3.0.6 on 2020-05-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0003_auto_20200526_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='id',
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
