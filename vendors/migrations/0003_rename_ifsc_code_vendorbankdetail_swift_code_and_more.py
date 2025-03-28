# Generated by Django 5.1.7 on 2025-03-29 19:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_alter_vendor_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendorbankdetail',
            old_name='ifsc_code',
            new_name='swift_code',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='description',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='seller_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterUniqueTogether(
            name='vendor',
            unique_together={('user', 'description', 'vendor_email', 'seller_name', 'store_name')},
        ),
        migrations.AlterUniqueTogether(
            name='vendorbankdetail',
            unique_together={('vendor', 'bank_name', 'account_number', 'swift_code')},
        ),
    ]
