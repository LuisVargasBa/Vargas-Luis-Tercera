# Generated by Django 5.1.1 on 2024-10-13 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('genero', models.CharField(max_length=25)),
                ('personaje', models.CharField(max_length=40)),
                ('anio', models.IntegerField()),
            ],
        ),
    ]
