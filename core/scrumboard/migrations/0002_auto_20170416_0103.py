# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirements',
            name='deadline',
            field=models.DateField(),
        ),
    ]
