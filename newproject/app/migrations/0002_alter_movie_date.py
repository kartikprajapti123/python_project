# Generated by Django 5.0 on 2024-01-08 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.CharField(default=datetime.datetime(2024, 1, 8, 16, 52, 5, 884835), max_length=100),
        ),
    ]