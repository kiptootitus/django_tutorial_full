# Generated by Django 5.1.7 on 2025-03-26 19:32

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None,
                                                                 unique=True),
        ),
    ]
