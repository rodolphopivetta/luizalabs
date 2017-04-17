# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows employees to be viewed.
    """
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer
