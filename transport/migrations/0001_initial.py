# Generated by Django 2.2.24 on 2022-01-24 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_type', models.CharField(choices=[('Pick-Up', 'Pick-Up'), ('Delivery', 'Delivery')], default='Pick-Up', max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='request_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
