# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-19 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20171215_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]