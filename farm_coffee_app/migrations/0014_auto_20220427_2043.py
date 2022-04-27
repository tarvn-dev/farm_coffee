# Generated by Django 3.2.3 on 2022-04-27 13:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farm_coffee_app', '0013_alter_products_pub_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='reviews',
            new_name='Review',
        ),
        migrations.RenameModel(
            old_name='toppings',
            new_name='Topping',
        ),
        migrations.RenameField(
            model_name='order_product',
            old_name='products_fk_product_id',
            new_name='product_fk_product_id',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='products_fk_products_id',
            new_name='product_fk_product_id',
        ),
    ]
