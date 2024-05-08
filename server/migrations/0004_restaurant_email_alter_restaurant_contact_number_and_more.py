# Generated by Django 4.1.13 on 2024-05-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_restaurant_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='email',
            field=models.EmailField(default='bla@gmail.com', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='contact_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='operating_hours',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
