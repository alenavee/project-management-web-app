from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Project, Task, EmployeePhoto
from .serializers import ProjectSerializer, TaskSerializer, EmployeePhotoSerializer
from django.contrib.auth.models import User

from department_app.models import Department
from client_app.models import Client
from django_filters import rest_framework as filters

from .filters import ProjectDateRangeFilter


class LeadPagination(PageNumberPagination):
    page_size = 3


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    pagination_class = LeadPagination
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter,)
    search_fields = ('project_name',)
    filterset_fields = ('start_date',)
    filterset_class = ProjectDateRangeFilter


    def get_queryset(self):
        department = Department.objects.filter(employees__in=[self.request.user]).first()
        status = self.request.query_params.get('project_status')
        if status:
            return self.queryset.filter(department=department, project_status=status)
        else:


            return self.queryset.filter(department=department)#, project_status=status)

    def perform_update(self, serializer):
        obj = self.get_object()
        # employee_id = self.request.data['assigned_to']
        # client_id = self.request.data['client']
        # user = User.objects.get(pk=employee_id)
        # client = Client.objects.get(pk=client_id)
        serializer.save()  # assigned_to=user, client=client)

    def perform_create(self, serializer):
        department = Department.objects.filter(employees__in=[self.request.user]).first()
        client_id = self.request.data['client']
        client = Client.objects.get(pk=client_id)

        assigned_to_id = self.request.data['assigned_to']
        assigned_to_id = User.objects.get(pk=assigned_to_id)

        serializer.save(department=department, employee=self.request.user, client=client, assigned_to=assigned_to_id)


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        project_id = self.request.GET.get('project_id')

        return self.queryset.filter(project_id=project_id)

    def perform_update(self, serializer):
        obj = self.get_object()
        employee_id = self.request.data['employee']
        if employee_id:
            user = User.objects.get(pk=employee_id)
            serializer.save(employee=user)

        else:
            serializer.save()

    def perform_create(self, serializer):
        # department = Department.objects.filter(employees__in=[self.request.user]).first()
        project_id = self.request.data['project_id']
        employee_id = self.request.data['employee']
        employee = User.objects.get(pk=employee_id)

        serializer.save(project_id=project_id, employee=employee)


@api_view(['POST'])
def delete_project(request, project_id):
    department = Department.objects.filter(employees__in=[request.user]).first()

    project = department.projects.filter(pk=project_id)
    project.delete()

    return Response({'message': 'The project was deleted'})


@api_view(['POST'])
def delete_task(request, project_id, task_id):
    department = Department.objects.filter(employees__in=[request.user]).first()

    project = department.projects.filter(pk=project_id)
    task = Task.objects.filter(pk=task_id)
    task.delete()

    return Response({'message': 'The task was deleted'})


@api_view(['GET'])
def get_my_tasks(request):
    tasks = Task.objects.filter(employee__in=[request.user]).all()
    serializer = TaskSerializer(tasks)

    return Response(serializer.data)


class PairByPriorityStatusListView(ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        pair_queryset = Project.objects.all()
        user = self.request.user

        if user.is_authenticated:
            priority = self.request.query_params.get('priority')
            status = self.request.query_params.get('project_status')

            pair_queryset = Project.objects.all()
            if priority and status:
                pair_queryset = pair_queryset.filter(priority=priority, project_status=status)

        return pair_queryset


class DateOrderedFilterView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (OrderingFilter,)
    filterset_fields = ('start_date',)


class ProjectSearchFilterView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('project_name',)


class ProjectDateRangeFilterView(ListAPIView):
    queryset =  Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectDateRangeFilter


# FILE UPLOAD
class EmployeePhotoCreateView(CreateAPIView):
    queryset = EmployeePhoto.objects.all()
    serializer_class = EmployeePhotoSerializer

# 2 AND MORE FILES UPLOAD
class MultipleEmployeePhotoCreateView(CreateAPIView):
    queryset = EmployeePhoto.objects.all()
    serializer_class = EmployeePhotoSerializer

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')

        for file in files:
            employee_id = request.user.id
            file = EmployeePhoto(
                employee=User.objects.get(id=employee_id),
                file=file)
            file.save()

        return Response(str(request.data), status=status.HTTP_201_CREATED)
