# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Departament, Employee


class EmployeeTestCase(APITestCase):
    def setUp(self):
        """
        Create departaments and employees to test
        """
        architecture = Departament.objects.create(departament='Architecture')
        ecommerce = Departament.objects.create(departament='E-commerce')
        mobile = Departament.objects.create(departament='Mobile')
        Employee.objects.create(
            name="Arnaldo Pereira",
            email="arnaldo@luizalabs.com",
            departament=architecture
        )
        Employee.objects.create(
            name="Renato Pedigoni",
            email="renato@luizalabs.com",
            departament=ecommerce
        )
        Employee.objects.create(
            name="Thiago Catoto",
            email="catoto@luizalabs.com",
            departament=mobile)

    def test_employees_exists(self):
        """
        Check if employees have been created
        """
        arnaldo = Employee.objects.get(name="Arnaldo Pereira")
        renato = Employee.objects.get(name="Renato Pedigoni")
        thiago = Employee.objects.get(name="Thiago Catoto")

    def test_employees_via_api(self):
        """
        Ensure we can get all employees from API.
        """
        response = self.client.get('/employee/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # employees are sorted by name, so get by list index is not a problem
        self.assertEqual(response.json()[0]['name'], 'Arnaldo Pereira')
        self.assertEqual(response.json()[1]['name'], 'Renato Pedigoni')
        self.assertEqual(response.json()[2]['name'], 'Thiago Catoto')
