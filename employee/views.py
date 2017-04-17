# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from employee.models import Departament, Employee
from employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows create, edit, delete or retrieve employees.
    """
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer
