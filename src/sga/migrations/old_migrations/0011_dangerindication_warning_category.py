# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-23 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sga', '0010_auto_20180822_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='dangerindication',
            name='warning_category',
            field=models.ManyToManyField(related_name='warningcategory', to='sga.WarningClass', verbose_name='Warning category'),
        ),
    ]