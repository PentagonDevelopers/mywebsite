# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-07-04 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managetrainer', '0004_auto_20190624_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='batches',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
