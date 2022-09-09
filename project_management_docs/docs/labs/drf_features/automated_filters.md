## Автоматические фильтры
### Фильтр проектов по дате
![Screenshot](img/date_order.PNG "Screenshot")
```python
class DateOrderedFilterView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (OrderingFilter,)
    filterset_fields = ('start_date',)
```

### Фильтр поиска проекта по названию
![Screenshot](img/project_search.PNG "Screenshot")
```python
class ProjectSearchFilterView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('project_name',)
```


### Фильтрация по дате в промежутке
![Screenshot](img/date-filter-range.PNG "Screenshot")
```python
class ProjectDateRangeFilterView(ListAPIView):
    queryset =  Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectDateRangeFilter

filter.py

class ProjectDateRangeFilter(filters.FilterSet):
    start_date_min = filters.DateFilter(field_name="start_date", lookup_expr='gte')
    start_date_max = filters.DateFilter(field_name="start_date", lookup_expr='lte')

    class Meta:
        model = Project
        fields = ['start_date']
```