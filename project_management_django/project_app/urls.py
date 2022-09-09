from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, delete_project, delete_task, get_my_tasks, PairByPriorityStatusListView, \
    DateOrderedFilterView, ProjectDateRangeFilterView, MultipleEmployeePhotoCreateView, ProjectSearchFilterView,\
    EmployeePhotoCreateView

#app_name = 'project_app'

router = DefaultRouter()
router.register(prefix='projects', viewset=ProjectViewSet, basename='projects')
router.register(prefix='tasks', viewset=TaskViewSet, basename='tasks')

urlpatterns = [
    path('departments/get_my_tasks/', get_my_tasks, name='get_my_tasks'),
    path('tasks/delete_task/<int:project_id>/<int:task_id>/', delete_task, name='delete_task'),
    path('projects/delete_project/<int:project_id>/', delete_project, name='delete_project'),

    # filters
    path('projects/get_priority_and_status/', PairByPriorityStatusListView.as_view()),
    path('projects/projects_ordered/', DateOrderedFilterView.as_view()),
    path('projects/project_search/', ProjectSearchFilterView.as_view(),  name='projects_search'),
    path('projects/project_range/', ProjectDateRangeFilterView.as_view()),

    path('employee_photo_upload/', EmployeePhotoCreateView.as_view()),
    path('multiple_employee_photo_upload/', MultipleEmployeePhotoCreateView.as_view()),
    path('', include(router.urls)),
]
