# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170116_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='ktheme',
            name='image',
            field=models.ImageField(default=None, upload_to=b''),
        ),
    ]