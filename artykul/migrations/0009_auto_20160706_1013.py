# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artykul', '0008_auto_20160704_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artykul',
            name='obrazy',
            field=models.ImageField(blank=True, upload_to='galleries'),
        ),
    ]
