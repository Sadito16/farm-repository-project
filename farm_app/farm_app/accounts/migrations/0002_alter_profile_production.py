# Generated by Django 4.1.4 on 2022-12-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='production',
            field=models.CharField(blank=True, choices=[('Vegetables or Fruits', 'Vegetables or Fruits'), ('Dairy products', 'Dairy products'), ('Animal products', 'Animal products'), ('Nuts', 'Nuts')], default='Vegetables or Fruits', max_length=20, null=True),
        ),
    ]
