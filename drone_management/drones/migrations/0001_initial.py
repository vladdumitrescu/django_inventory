# Generated by Django 3.2.8 on 2021-10-20 12:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CameraBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('brand', models.CharField(max_length=200)),
                ('serial_number', models.CharField(max_length=200)),
                ('camera_model', models.CharField(max_length=200)),
                ('camera_megapixel', models.CharField(max_length=200)),
                ('camera_brand', models.CharField(max_length=200)),
                ('camera_brand_filter', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='drones.camerabrand')),
            ],
        ),
    ]
