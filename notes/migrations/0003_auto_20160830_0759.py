# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='pin',
            field=models.BooleanField(default=False),
        ),
    ]
