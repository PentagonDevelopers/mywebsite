# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-07-17 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managetrainer', '0007_remove_trainer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='profile_pic',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
