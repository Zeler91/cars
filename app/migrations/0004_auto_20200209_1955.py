# Generated by Django 3.0.3 on 2020-02-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_car_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='last_year',
            field=models.SmallIntegerField(blank=True, verbose_name='Until year'),
        ),
        migrations.AlterField(
            model_name='car',
            name='release_year',
            field=models.SmallIntegerField(blank=True, verbose_name='Since year'),
        ),
    ]
