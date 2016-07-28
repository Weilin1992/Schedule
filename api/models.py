from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User)
    GENDER_CHOICES = (
            ('M','Male'),
            ('F','Female'),
            )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
