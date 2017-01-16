# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-13 11:54
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20170113_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('theme', 'l', 'b', 'h')),
        ),
    ]