from django.db import models
from django.contrib.auth.models import User

from department_app.models import Department
from client_app.models import Client
from .validators import validate_file_size, validate_file_type


class Project(models.Model):
    NEW = 'new'
    IN_PROGRESS = 'inprogress'
    CANCELLED = 'cancelled'
    FINISHED = 'finished'
    FROZEN = 'frozen'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (CANCELLED, 'Cancelled'),
        (FINISHED, 'Finished'),
        (FROZEN, 'Frozen'),
    )

    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high')
    )

    department = models.ForeignKey(Department, related_name="projects", on_delete=models.CASCADE, blank=True, null=True)
    project_name = models.CharField(max_length=255)
    project_status = models.CharField(max_length=25, choices=CHOICES_STATUS, default=NEW)
    priority = models.CharField(max_length=25, choices=CHOICES_PRIORITY, default=MEDIUM)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    assigned_to = models.ForeignKey(User, related_name='assignedprojects', blank=True, null=True,
                                    on_delete=models.SET_NULL)
    project_description = models.TextField(max_length=400, blank=True, null=True)
    employee = models.ForeignKey(User, related_name='project_app', blank=True, null=True,
                                 on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, related_name='project_app', on_delete=models.CASCADE, blank=True, null=True)


class Task(models.Model):
    # department = models.ForeignKey(Department, related_name="projects", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)

    NEW = 'new'
    IN_PROGRESS = 'inprogress'
    CANCELLED = 'cancelled'
    FINISHED = 'finished'
    FROZEN = 'frozen'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (IN_PROGRESS, 'In progress'),
        (CANCELLED, 'Cancelled'),
        (FINISHED, 'Finished'),
        (FROZEN, 'Frozen')
    )

    status = models.CharField(max_length=25, choices=CHOICES_STATUS, default=NEW)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    name = models.TextField(max_length=400, blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)
    employee = models.ForeignKey(User, related_name='assignedtasks', blank=True, null=True,
                                 on_delete=models.SET_NULL)


def get_upload_path(instance, filename):
    return f'employee_photo/employee_{instance.employee.id}/{filename}'


class EmployeePhoto(models.Model):
    employee = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='employee_photos')
    file = models.FileField(
        validators=[validate_file_size, validate_file_type],
        upload_to=get_upload_path
    )
    file_name = models.CharField(max_length=100, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Photo of {str(self.user)}'

    def save(self, *args, **kwargs):
        self.file_name = self.file.name
        self.file_size = self.file.size
        super(EmployeePhoto, self).save(*args, **kwargs)
