# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-07-16 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managetrainer', '0005_batches_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='profile_pic',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
