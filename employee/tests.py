from django.test import TestCase
from .models import Employee
import pytest
from mixer.backend.django import mixer
# Create your tests here.
pytestmark = pytest.mark.django_db

class TestEmployeeModel(TestCase):

    def setUp(self) -> None:
        # setting up new employee
        self.employee1 = Employee.objects.create(
                    emp_no=555,
                    emp_name="John Doe",
                    emp_address="Pune",
                    emp_salary=50000,
                    emp_position="software_engineer",
                    emp_present=True)

    #Test Create Functionality
    def test_employee_create(self):
        employee_result = Employee.objects.last()
        assert employee_result.emp_name == "John Doe"

    #Test status (Absent)
    def test_employee_status_absent(self):
        employee_result = Employee.objects.last()
        assert employee_result.get_status() == "Present"

    # Test status (Present)
    def test_employee_status_present(self):
        employee_result = Employee.objects.last()
        employee_result.emp_present = False
        employee_result.save()
        assert employee_result.get_status() == "Absent"

    def test_employee_str(self):
        employee_result = Employee.objects.last()
        assert str(employee_result) == "555"



