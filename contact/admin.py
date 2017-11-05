# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import (
        Contact,
        Address,
        SocialAccount,
        SpecialDate,
        Note,
        Communication
)

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('salutation', 'first_name', 'middle_name', 'last_name', 'job_title', 'industry', 'email', 'phone', 'last_update', 'created')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'industry', 'job_title')
    list_per_page = 100

admin.site.register(Contact, ContactAdmin)
