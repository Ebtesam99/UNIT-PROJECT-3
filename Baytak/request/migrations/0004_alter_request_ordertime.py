# Generated by Django 5.0 on 2023-12-10 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_alter_request_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='orderTime',
            field=models.DateTimeField(),
        ),
    ]
