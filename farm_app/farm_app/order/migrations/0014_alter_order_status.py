# Generated by Django 4.1.4 on 2024-02-04 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_order_address_alter_order_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Ordered', 'Ordered'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Ordered', max_length=20),
        ),
    ]
