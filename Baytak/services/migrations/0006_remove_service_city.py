# Generated by Django 5.0 on 2023-12-13 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_service_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='city',
        ),
    ]