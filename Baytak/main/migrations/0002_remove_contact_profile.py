# Generated by Django 5.0 on 2023-12-11 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='profile',
        ),
    ]