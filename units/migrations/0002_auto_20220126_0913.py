# Generated by Django 2.2.24 on 2022-01-26 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]