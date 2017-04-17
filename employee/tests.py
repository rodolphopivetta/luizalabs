# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Departament, Employee
from employee.serializers import EmployeeSerializer


class BaseEmployeeTestCase(APITestCase):
    def setUp(self):
        departament = Departament.objects.create(departament='Architecture')
        self.employee = Employee.objects.create(**{
            'name': 'Arnaldo Pereira',
            'email': 'arnaldo@luizalabs.com',
            'departament': departament
        })
        self.data = EmployeeSerializer(self.employee).data


class CreateEmployeeTestCase(BaseEmployeeTestCase):
    def setUp(self):
        """
        Ensure we will create another employee with another departament
        """
        super(self.__class__, self).setUp()
        self.data.update({
            'name': 'Renato Pedigoni',
            'departament': 'E-commerce'
        })

    def test_can_create_employee(self):
        """
        Ensure we can create employee.
        """
        url = reverse('employee-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadEmployeeTestCase(BaseEmployeeTestCase):
    def test_can_read_employee_list(self):
        """
        Ensure we can read employee list.
        """
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), Employee.objects.count())

    def test_can_read_employee_detail(self):
        """
        Ensure we can read employee detail.
        """
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateEmployeeTestCase(BaseEmployeeTestCase):
    def test_can_update_employee(self):
        """
        Ensure we can update employee.
        """

        self.data.update({'departament': 'Mobile'})
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.put(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteEmployeeTestCase(BaseEmployeeTestCase):
    def test_can_delete_employee(self):
        """
        Ensure we can delete employee.
        """
        url = reverse('employee-detail', args=[self.employee.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
