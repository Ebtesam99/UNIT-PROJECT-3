# Generated by Django 5.0 on 2023-12-10 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
        ('services', '0004_alter_service_name_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='service',
        ),
        migrations.AddField(
            model_name='request',
            name='service',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='services.service'),
            preserve_default=False,
        ),
    ]