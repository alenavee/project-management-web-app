from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=255)
    employees = models.ManyToManyField(User, related_name='departments')
    lead = models.ForeignKey(User, related_name='department_lead', on_delete=models.CASCADE)
