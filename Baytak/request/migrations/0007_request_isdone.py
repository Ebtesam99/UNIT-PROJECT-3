# Generated by Django 5.0 on 2023-12-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0006_request_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]
