# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_auto_20160924_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='password2',
            field=models.CharField(default=1, max_length=100),
        ),
    ]