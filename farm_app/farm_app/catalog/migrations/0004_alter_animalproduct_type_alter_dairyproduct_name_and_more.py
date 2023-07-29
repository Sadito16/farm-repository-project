# Generated by Django 4.1.4 on 2023-07-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_animalproduct_price_nut_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalproduct',
            name='type',
            field=models.CharField(choices=[('Chicken', 'CHICKEN'), ('Pig', 'PIG'), ('Cow', 'COW'), ('Goat', 'GOAT'), ('Sheep', 'SHEEP'), ('Turkey', 'TURKEY'), ('Goose', 'GOOSE'), ('Rabbit', 'RABBIT'), ('Horse', 'HORSE'), ('Donkey', 'DONKEY'), ('Lamb', 'LAMB'), ('Other', 'OTHER')], default='Other', max_length=7),
        ),
        migrations.AlterField(
            model_name='dairyproduct',
            name='name',
            field=models.CharField(choices=[('Milk', 'MILK'), ('Butter', 'BUTTER'), ('Cheese', 'CHEESE'), ('Curd', 'CURD'), ('Yogurt', 'YOGURT'), ('Other', 'OTHER')], default='Other', max_length=6),
        ),
        migrations.AlterField(
            model_name='nut',
            name='type',
            field=models.CharField(choices=[('Roasted', 'ROASTED'), ('Row', 'RAW'), ('Dried', 'DRIED_FRUIT'), ('Other', 'OTHER')], default='Other', max_length=7),
        ),
        migrations.AlterField(
            model_name='vegetableandfruit',
            name='name',
            field=models.CharField(choices=[('Carrot', 'CARROT'), ('Potato', 'POTATO'), ('Cabbage', 'CABBAGE'), ('Cauliflower', 'CAULIFLOWER'), ('Cucumber', 'CUCUMBERS'), ('Tomato', 'TOMATO'), ('Onion', 'ONION'), ('Broccoli', 'BROCCOLI'), ('Eggplant', 'EGGPLANT'), ('Pepper', 'PEPPER'), ('Corn', 'CORN'), ('Pumpkin', 'PUMPKIN'), ('Apple', 'APPLE'), ('Grape', 'GRAPE'), ('Strawberry', 'STRAWBERRY'), ('Pear', 'PEAR'), ('Plum', 'PLUM'), ('Orange', 'ORANGE'), ('Cherry', 'CHERRY'), ('Blackberry', 'BLACKBERRY'), ('Lemon', 'LEMON'), ('Peach', 'PEACH'), ('Melon', 'MELON'), ('Watermelon', 'WATERMELON'), ('Other', 'OTHER')], default='Other', max_length=11),
        ),
    ]