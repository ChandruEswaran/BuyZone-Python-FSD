# Generated by Django 5.1.1 on 2024-11-11 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_orginal_price_product_original_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='products_image',
        ),
    ]
