# Generated by Django 5.0 on 2023-12-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobileNumber',
            field=models.IntegerField(null=True),
        ),
    ]
