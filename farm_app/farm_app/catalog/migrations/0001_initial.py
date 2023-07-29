# Generated by Django 4.1.4 on 2023-07-29 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Dried fruit', 'Dried fruit'), ('Roasted', 'Roasted'), ('Row', 'Row'), ('Seeds', 'Seeds'), ('Other', 'Other')], default='Other', max_length=11)),
                ('name', models.CharField(max_length=35)),
                ('package', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Chicken', 'Chicken'), ('Cow', 'Cow'), ('Horse', 'Horse'), ('Donkey', 'Donkey'), ('Goat', 'Goat'), ('Goose', 'Goose'), ('Lamb', 'Lamb'), ('Pig', 'Pig'), ('Rabbit', 'Rabbit'), ('Sheep', 'Sheep'), ('Turkey', 'Turkey'), ('Other', 'Other')], default='Other', max_length=7)),
                ('name', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField(blank=True, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VegetableAndFruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Orange', 'Orange'), ('Other', 'Other'), ('Watermelon', 'Watermelon'), ('Melon', 'Melon'), ('Peach', 'Peach'), ('Lemon', 'Lemon'), ('Blackberry', 'Blackberry'), ('Cherry', 'Cherry'), ('Plum', 'Plum'), ('Pear', 'Pear'), ('Strawberry', 'Strawberry'), ('Grape', 'Grape'), ('Carrot', 'Carrot'), ('Apple', 'Apple'), ('Pumpkin', 'Pumpkin'), ('Corn', 'Corn'), ('Pepper', 'Pepper'), ('Eggplant', 'Eggplant'), ('Broccoli', 'Broccoli'), ('Onion', 'Onion'), ('Tomato', 'Tomato'), ('Cucumber', 'Cucumber'), ('Cauliflower', 'Cauliflower'), ('Cabbage', 'Cabbage'), ('Potato', 'Potato')], default='Other', max_length=11)),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name')},
            },
        ),
        migrations.CreateModel(
            name='DairyProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Butter', 'Butter'), ('Cheese', 'Cheese'), ('Curd', 'Curd'), ('Milk', 'Milk'), ('Yogurt', 'Yogurt'), ('Other', 'Other')], default='Other', max_length=6)),
                ('percent', models.IntegerField()),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name')},
            },
        ),
    ]