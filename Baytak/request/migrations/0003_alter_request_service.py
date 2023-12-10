# Generated by Django 5.0 on 2023-12-10 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_remove_request_service_request_service'),
        ('services', '0004_alter_service_name_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
    ]
