# Generated by Django 3.2.3 on 2022-04-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_coffee_app', '0010_remove_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]