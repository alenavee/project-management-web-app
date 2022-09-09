from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Client
from .serializers import ClientSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from department_app.models import Department


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    filter_backends = (SearchFilter,)
    search_fields = ('name', 'contact_person','email','phone_number',)

    def get_queryset(self):
        department = Department.objects.filter(employees__in=[self.request.user]).first()

        return self.queryset.filter(department=department)


    def perform_create(self, serializer):
        department = Department.objects.filter(employees__in=[self.request.user]).first()
        serializer.save(department=department)

@api_view(['POST'])
def delete_client(request, client_id):
    department = Department.objects.filter(employees__in=[request.user]).first()

    client = department.clients.filter(pk=client_id)
    client.delete()

    return Response({'message': 'The client was deleted'})

# Create your views here.
