# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from employee.models import Departament, Employee


class EmployeeSerializer(serializers.ModelSerializer):
    departament = serializers.CharField(source='departament.departament')

    def create(self, validated_data):
        validated_data['departament'], _ = Departament.objects.get_or_create(
            departament=validated_data['departament']['departament']
        )
        employee = Employee.objects.create(**validated_data)
        return employee

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        departament = validated_data['departament']['departament']
        instance.departament, _ = Departament.objects.get_or_create(
            departament=departament or instance.departament.departament
        )
        instance.save()
        return instance

    class Meta:
        model = Employee
        fields = ('name', 'email', 'departament',)
