# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BerryBear', '0003_program_other_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='commands',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
