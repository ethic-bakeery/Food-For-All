# Generated by Django 4.1.13 on 2024-05-07 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_restaurant_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='last_login',
        ),
    ]
