# Generated by Django 4.1.7 on 2023-03-19 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_location_filmonlocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='actedinfilm',
            name='payment',
            field=models.IntegerField(default=10000000),
            preserve_default=False,
        ),
    ]
