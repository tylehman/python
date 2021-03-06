# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class JobInfo(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    comp_name = models.CharField(max_length=50, blank=True, null=True)
    job_addr = models.CharField(max_length=50, blank=True, null=True)
    job_link = models.CharField(max_length=50, blank=True, null=True)
    job_posted = models.DateField(null=True)
    job_search = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_info'
