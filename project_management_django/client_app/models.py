from django.db import models
from django.contrib.auth.models import User

from department_app.models import Department


class Client(models.Model):

    department = models.ForeignKey(Department, related_name="clients", on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
