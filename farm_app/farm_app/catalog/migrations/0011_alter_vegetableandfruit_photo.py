# Generated by Django 4.1.4 on 2023-08-08 17:03

from django.db import migrations, models
import farm_app.catalog.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_vegetableandfruit_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vegetableandfruit',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos', validators=[farm_app.catalog.validators.validate_image_size]),
        ),
    ]
