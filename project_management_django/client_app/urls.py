from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, delete_client

app_name='client_app'

router = DefaultRouter()
router.register(prefix='clients', viewset=ClientViewSet, basename='clients')


urlpatterns = [
    path('clients/delete_client/<int:client_id>/', delete_client, name='delete_client'),
    path('', include(router.urls))
]
