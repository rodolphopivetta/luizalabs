# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Departament(models.Model):
    departament = models.CharField(max_length=100)

    def __str__(self):
        return self.departament


class Employee(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    departament = models.ForeignKey(Departament, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
