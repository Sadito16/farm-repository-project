# Generated by Django 4.1.4 on 2023-07-31 20:06

from django.db import migrations, models
import farm_app.catalog.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_publication_date_animalproduct_date_of_publication_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalproduct',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos', validators=[farm_app.catalog.validators.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='dairyproduct',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos', validators=[farm_app.catalog.validators.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='nut',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos', validators=[farm_app.catalog.validators.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='vegetableandfruit',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos', validators=[farm_app.catalog.validators.validate_image_size]),
        ),
    ]
