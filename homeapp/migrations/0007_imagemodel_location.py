# Generated by Django 4.2.8 on 2024-12-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0006_imagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='location',
            field=models.CharField(default='default_value', max_length=50),
        ),
    ]
