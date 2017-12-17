# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Program(models.Model):
    name = models.CharField(max_length=200)
    commands = models.CharField(max_length=2000)

    def __str__(self):
        return self.name