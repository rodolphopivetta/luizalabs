# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from employee.models import Departament, Employee


class DepartamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departament
        fields = ('departament',)


class EmployeeSerializer(serializers.ModelSerializer):
    departament = serializers.StringRelatedField(many=False)

    class Meta:
        model = Employee
        fields = ('name', 'email', 'departament',)
