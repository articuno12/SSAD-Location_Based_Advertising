# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 14:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_auto_20161103_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadadvetisement',
            name='start_week',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 3, 14, 51, 50, 811216, tzinfo=utc), verbose_name='Starting week of the advertisement'),
        ),
    ]
