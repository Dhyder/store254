# Generated by Django 2.2.24 on 2022-01-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0003_auto_20220120_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
