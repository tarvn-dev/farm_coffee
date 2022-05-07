# Generated by Django 3.2.3 on 2022-05-07 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm_coffee_app', '0006_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='farm_coffee_app.product')),
                ('total_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farm_coffee_app.total_order')),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('item', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='farm_coffee_app.item')),
            ],
        ),
    ]