# Generated by Django 4.1.4 on 2023-08-18 11:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_farmeruser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmeruser',
            name='first_name',
            field=models.CharField(blank=True, max_length=25, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'The value should contain only letters.')]),
        ),
        migrations.AlterField(
            model_name='farmeruser',
            name='last_name',
            field=models.CharField(blank=True, max_length=25, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'The value should contain only letters.')]),
        ),
    ]
