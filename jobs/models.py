# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

def make_choices(values):
    return [(v, v) for v in values]

class JobInfo(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    comp_name = models.CharField(max_length=50, blank=True, null=True)
    job_addr = models.CharField(max_length=50, blank=True, null=True)
    job_link = models.CharField(max_length=50, blank=True, null=True)
    job_posted = models.CharField(max_length=50, blank=True, null=True)
    job_search = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.job_title

    class Meta:
        managed = True
        db_table = 'job_info'
