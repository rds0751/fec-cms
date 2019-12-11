# -*- coding: utf-8 -*-

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Contact

class ContactResource(resources.ModelResource):

    class Meta:
        model = Contact

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('email',)
    resource_class = ContactResource
# Register your models here.
admin.site.register(Contact, ContactAdmin)


