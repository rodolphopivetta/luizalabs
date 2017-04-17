# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from employee.models import Departament, Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'departament')
    search_fields = ('name',)
    list_filter = ('departament',)
    ordering = ('name',)


admin.site.register(Departament)
admin.site.register(Employee, EmployeeAdmin)
