# Generated by Django 4.1.4 on 2023-08-17 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_remove_animalproduct_package_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animalproduct',
            name='date_of_publication',
        ),
        migrations.RemoveField(
            model_name='dairyproduct',
            name='publication_date',
        ),
        migrations.RemoveField(
            model_name='nut',
            name='publication_date',
        ),
        migrations.RemoveField(
            model_name='vegetableandfruit',
            name='publication_date',
        ),
    ]