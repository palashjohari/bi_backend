# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170116_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='ktheme',
            name='desc',
            field=models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam malesuada adipiscing tincidunt.', max_length=100, verbose_name='Description'),
        ),
    ]