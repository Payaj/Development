# Generated by Django 3.0.6 on 2020-06-02 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FIRSTAPP', '0002_auto_20200602_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_Time', models.DateTimeField()),
                ('call_duration_minute', models.IntegerField()),
                ('phone_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FIRSTAPP.ContactInfo')),
            ],
            options={
                'verbose_name_plural': 'CallInfo',
            },
        ),
    ]
