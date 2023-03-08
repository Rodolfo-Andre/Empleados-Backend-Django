from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Employee
from .pagination import CustomPagination

class EmployeeView(ModelViewSet):
  queryset = Employee.objects.all()
  permission_classes = [IsAuthenticated]
  pagination_class = CustomPagination
  serializer_class = EmployeeSerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ['first_name', 'last_name']
  ordering = ['last_name']
  
