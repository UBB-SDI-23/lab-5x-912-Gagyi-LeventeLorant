# Generated by Django 4.1.7 on 2023-03-19 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_actedinfilm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('is_outdoors', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FilmOnLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locationfilm', to='films.film')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='films.location')),
            ],
        ),
    ]
