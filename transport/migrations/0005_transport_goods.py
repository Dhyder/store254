# Generated by Django 2.2.24 on 2022-01-26 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
        ('transport', '0004_transport_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='goods',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='units.Goods'),
        ),
    ]
