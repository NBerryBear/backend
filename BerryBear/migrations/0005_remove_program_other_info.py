# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BerryBear', '0004_program_commands'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='other_info',
        ),
    ]
