# Generated by Django 4.1.4 on 2023-11-27 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_orderitem_dairy_alter_orderitem_fruit_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_at',)},
        ),
    ]
