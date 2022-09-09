from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, UserDetail, get_my_department, add_employee, UserList

router = DefaultRouter()
router.register(prefix='departments', viewset=DepartmentViewSet, basename='departments')

urlpatterns = [
    path('users_list/',  UserList.as_view()),
    path('departments/employee/<int:pk>/', UserDetail.as_view(), name='userdetail'),
    path('departments/get_my_department/', get_my_department, name='get_my_department'),
    path('departments/add_employee/', add_employee, name='add_employee'),
    path('', include(router.urls)),

]

