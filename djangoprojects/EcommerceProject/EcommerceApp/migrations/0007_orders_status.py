# Generated by Django 4.2.3 on 2023-09-05 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceApp', '0006_remove_orders_cart_orders_price_orders_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
