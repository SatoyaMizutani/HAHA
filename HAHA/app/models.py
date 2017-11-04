"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField("username",max_length=300)
    password = models.CharField("username",max_length=300)
