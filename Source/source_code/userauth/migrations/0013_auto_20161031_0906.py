# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 09:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0012_auto_20161029_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadadvetisement',
            name='start_week',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 31, 9, 6, 45, 591274, tzinfo=utc), verbose_name='Starting week of the advertisement'),
        ),
    ]