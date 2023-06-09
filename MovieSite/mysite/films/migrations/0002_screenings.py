# Generated by Django 4.1.7 on 2023-03-12 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screenings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='Screening date')),
                ('imax', models.BooleanField(default=False)),
                ('tickets_bought', models.IntegerField()),
                ('price', models.FloatField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
            ],
        ),
    ]
