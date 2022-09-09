from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Department


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )


class DepartmentSerializer(serializers.ModelSerializer):
    employees = UserSerializer(many=True, read_only=True)
    lead = UserSerializer(read_only=True)

    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "employees",
            "lead",
        )

