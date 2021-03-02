from django.shortcuts import render
from .serializers import EmployeeSerializer
from employee.models import Employee
from rest_framework import viewsets
from rest_framework import permissions,authentication

# Create your views here.

class EmployeeCRUDAPIView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    

