# Generated by Django 4.1.7 on 2023-04-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_actedinfilm_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='description',
            field=models.CharField(default='-', max_length=500),
            preserve_default=False,
        ),
    ]