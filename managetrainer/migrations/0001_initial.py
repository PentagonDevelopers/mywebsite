# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-06-21 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_code', models.CharField(max_length=10)),
                ('batch_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=45)),
                ('designation', models.CharField(max_length=45)),
                ('salary', models.FloatField()),
                ('doj', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='batches',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managetrainer.Trainer'),
        ),
    ]
