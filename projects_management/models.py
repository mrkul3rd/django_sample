from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Project(models.Model):
    """Information about Project"""
    # id = models.CharField(primary_key=True, max_length=10)
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.project_name

@python_2_unicode_compatible  # only if you need to support Python 2
class Employee(models.Model):
    """Information about Employee"""
    # id = models.CharField(primary_key=True, max_length=10)
    id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name
