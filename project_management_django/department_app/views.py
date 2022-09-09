from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets, status
from django.http import Http404
from rest_framework.generics import ListAPIView

from .models import Department
from .serializers import DepartmentSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.views import APIView


# Create your views here.


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get_queryset(self):
        return self.queryset.filter(employees__in=[self.request.user]).first()

    def perform_create(self, serializer):
        obj = serializer.save(lead=self.request.user)
        obj.employees.add(self.request.user)
        obj.save()


class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_my_department(request):
    department = Department.objects.filter(employees__in=[request.user]).first()
    serializer = DepartmentSerializer(department)

    return Response(serializer.data)


@api_view(['POST'])
def add_employee(request):
    department = Department.objects.filter(employees__in=[request.user]).first()
    email = request.data['email']
    #print(email)
    user = User.objects.get(pk=email)
    department.employees.add(user)
    department.save()
    return Response()
