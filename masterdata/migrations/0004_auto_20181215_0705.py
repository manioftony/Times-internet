# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-15 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0003_auto_20181215_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
