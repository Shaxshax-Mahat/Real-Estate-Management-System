# Generated by Django 4.2.8 on 2024-12-07 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_alter_contact_email_alter_contact_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='default_value', max_length=50),
        ),
    ]
