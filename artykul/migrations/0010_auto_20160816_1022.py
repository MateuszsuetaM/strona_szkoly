# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-16 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artykul', '0009_auto_20160706_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artykul',
            name='obrazy',
            field=models.ImageField(blank=True, upload_to='galleries/'),
        ),
    ]
