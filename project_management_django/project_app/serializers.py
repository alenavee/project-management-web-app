from rest_framework import serializers

from .models import Project, Task, EmployeePhoto

from department_app.serializers import UserSerializer
from client_app.serializers import ClientSerializer


class ProjectSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Project
        read_only_fields = (
            'employee',
        )

        fields = (
            'id',
            'project_name',
            'project_status',
            'priority',
            'start_date',
            'end_date',
            'assigned_to',
            'client',
            'project_description'
        )


class TaskSerializer(serializers.ModelSerializer):
    employee = UserSerializer(read_only=True)

    class Meta:
        model = Task

        fields = (
            'id',
            'name',
            'employee',
            'status',
            'start_date',
            'end_date',
            'description',
        )


class EmployeePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePhoto
        fields = ['employee', 'file']

