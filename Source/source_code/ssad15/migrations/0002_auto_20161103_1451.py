# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 14:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ssad15', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='running_slots',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 3, 14, 51, 12, 786233, tzinfo=utc), verbose_name='Starting week of the advertisement'),
        ),
    ]
