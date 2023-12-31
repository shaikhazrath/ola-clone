# Generated by Django 4.2.7 on 2023-11-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_location_car_city_car_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default=100, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, default=100, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, help_text='Profile Picture', null=True, upload_to='car_images/', verbose_name='Profile Picture'),
        ),
    ]
