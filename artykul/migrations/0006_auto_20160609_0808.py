# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-09 06:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artykul', '0005_remove_kategoria_opis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artykul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=30)),
                ('teaser', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('data_dodania', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_zmiany', models.DateTimeField(default=django.utils.timezone.now)),
                ('wyroznione', models.BooleanField()),
                ('obrazy', models.ImageField(blank=True, upload_to='zdjecia')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='kategoria',
            name='nazwa',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='artykul',
            name='kategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artykul.Kategoria'),
        ),
    ]
