
from django_filters import rest_framework as filters, DateFromToRangeFilter
from .models import Project


class ProjectDateRangeFilter(filters.FilterSet):
    #start_date_min = filters.DateFilter(name="start_date", lookup_expr='gte')
    #start_date_max = filters.DateFilter(name="start_date", lookup_expr='lte')
    start_date = DateFromToRangeFilter()
    #start_date = filters.DateFilter(name='start_date', lookup_type=('gt'), )
    #end_date = filters.DateFilter(name='start_date', lookup_type=('lt'))
    #date_range = filters.DateRangeFilter(name='start_date')

    class Meta:
        model = Project
        fields = ['start_date']
