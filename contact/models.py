# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=140)
    middle_name = models.CharField(max_length=140, blank=True, null=True)
    last_name = models.CharField(max_length=140)
    job_title = models.CharField(max_length=140, blank=True, null=True)
    industry = models.CharField(max_length=140, blank=True, null=True)
    salutation = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=120, blank=True, null=True)
    created = models.DateTimeField(default=datetime.datetime.utcnow)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.first_name + self.last_name

ADDRESS_CHOICES = (
    ("WORK", "Work"),
    ("HOME", "Home")
)
class Address(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200, blank=True, null=True)
    postcode = models.CharField(max_length=100, blank=True, null=True)
    house_no = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    note = models.TextField(blank=True, null=True)
    address_type = models.CharField(max_length=150, choices=ADDRESS_CHOICES)

MEDIUM_CHOICES = (
    ("LINKEDIN", "LINKEDIN"),
    ("TWITTER", "Twitter"),
    ("GITHUB", "GitHub"),
    ("MEDIUM", "Medium"),
    ("FACEBOOK", "Facebook"),
    ("EMAIL", "Email"),
    ("PHONE", "Phone"),
    ("FACE2FACE", "Face to face"),
    ("POST", "Post"),
)
class SocialAccount(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    username = models.CharField(max_length=300)
    url = models.CharField(max_length=300, blank=True, null=True)
    medium = models.CharField(max_length=50, choices=MEDIUM_CHOICES)
    created = models.DateTimeField(default=datetime.datetime.utcnow)
    last_update = models.DateTimeField(auto_now=True)

OCCASION_CHOICES = (
    ("BIRTHDAY", "Birthday"),
    ("WORK_ANNIVERSARY", "Work Anniversary"),
    ("WEDDING_ANNIVERSARY", "Wedding Anniversary"),
    ("BIRTHDAY_OF_RELATION", "Birthday of a loved one"),
)
class SpecialDate(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    date = models.DateField()
    occasion = models.CharField(max_length=100, choices=OCCASION_CHOICES)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(default=datetime.datetime.utcnow)
    last_update = models.DateTimeField(auto_now=True)

class Note(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    note = models.TextField()
    created = models.DateTimeField(default=datetime.datetime.utcnow)
    last_update = models.DateTimeField(auto_now=True)

class Communication(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    note = models.TextField()
    medium = models.CharField(max_length=200, choices=MEDIUM_CHOICES)
    created = models.DateTimeField(default=datetime.datetime.utcnow)
    last_update = models.DateTimeField(auto_now=True)
