# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-04 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artykul', '0007_auto_20160610_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artykul',
            name='zawartosc',
            field=models.TextField(max_length=200),
        ),
    ]