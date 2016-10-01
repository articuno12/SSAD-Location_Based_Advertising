# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ssad15', '0003_auto_20160920_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='slot_id',
        ),
        migrations.AddField(
            model_name='slot',
            name='advertisement_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ssad15.advertisement'),
        ),
        migrations.AddField(
            model_name='slot',
            name='bundles_used',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='zone',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
        ),
    ]