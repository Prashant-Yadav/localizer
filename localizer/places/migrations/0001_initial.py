# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('mimetype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50)),
                ('geo_location', models.CharField(max_length=100)),
                ('place_id', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('local_phone_number', models.IntegerField()),
                ('international_phone_number', models.IntegerField()),
                ('website', models.URLField()),
                ('icon', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Place'),
        ),
    ]
