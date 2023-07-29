# Generated by Django 4.1.4 on 2023-07-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_animalproduct_publication_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalproduct',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nut',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dairyproduct',
            name='percent',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dairyproduct',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nut',
            name='type',
            field=models.CharField(choices=[('Dried', 'Dried'), ('Roasted', 'Roasted'), ('Row', 'Row'), ('Other', 'Other')], default='Other', max_length=7),
        ),
        migrations.AlterField(
            model_name='vegetableandfruit',
            name='price',
            field=models.FloatField(),
        ),
    ]