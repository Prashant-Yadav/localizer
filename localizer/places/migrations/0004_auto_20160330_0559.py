# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-30 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20160330_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='international_phone_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='local_phone_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
