from rest_framework import serializers

from .models import Client

from department_app.serializers import UserSerializer

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client

        fields = (
            'id',
            'name',
            'address',
            'contact_person',
            'email',
            'phone_number'
        )