# Generated by Django 4.1.4 on 2023-08-18 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_alter_animalproduct_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vegetableandfruit',
            unique_together=set(),
        ),
    ]
