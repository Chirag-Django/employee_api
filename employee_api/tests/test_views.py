import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from mixer.backend.django import mixer
from employee.models import Employee
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

pytestmark = pytest.mark.django_db


class TestEmployeeCRUDAPIView(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        # Setup for Token Authentication
        from rest_framework.authtoken.models import Token

        #Create Test User
        self.testUser = User.objects.create_user(username='testuser',password='something123')

        self.token = Token.objects.create(user=self.testUser)

        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)


    # Testing List API ViewSet
    def test_employee_api_list(self):
        #Create Two Employees/Resources using mixer
        employee1 = mixer.blend(Employee,emp_name='John Doe')
        employee2 = mixer.blend(Employee,emp_name='Jane Doe')

        #Call URL
        url = reverse('emp-api-list')
        response = self.client.get(url)

        # Check if resource Created or not
        assert response.json != None

        # Check if list has 2 resources or not
        assert len(response.json()) == 2

        # Affirm status Code for Get Resource
        assert response.status_code == 200

    # Testing Create API ViewSet
    def test_employee_api_create(self):
        #create an employee
        data_required = {
            "emp_no": "999",
            "emp_name": "Test Name",
            "emp_address": "Test Address",
            "emp_salary": 50000,
            "emp_position": "team_lead",
            "emp_present": True,
        }

        #Call URL
        url = reverse('emp-api-list')
        response = self.client.post(url,data=data_required)

        # Check if resource Created or not
        assert response.json != None

        # Affirm status Code for Create Resource
        assert response.status_code == 201

        #Affirm no of resoources created
        assert Employee.objects.count() == 1

    # Testing Detail API ViewSet
    def test_employee_api_detail(self):
        #Create Two Employees/Resources using mixer
        employee1 = mixer.blend(Employee,emp_name='John Doe')
        employee2 = mixer.blend(Employee, emp_name='Jane Doe')

        #Call URL
        url1 = reverse('emp-api-detail',kwargs={'pk':1})
        response1 = self.client.get(url1)
        url2 = reverse('emp-api-detail',kwargs={'pk':2})
        response2 = self.client.get(url2)

        # Check if resource Created or not
        assert response1.json != None
        assert response2.json != None

        # Affirm status Code for Create Resource
        assert response1.status_code == 200
        assert response2.status_code == 200

        #Affirm employee names
        assert response1.json()['emp_name'] == 'John Doe'
        assert response2.json()['emp_name'] == 'Jane Doe'


    # Testing Update API ViewSet
    def test_employee_api_update(self):
        #Create An Employees/Resource using mixer
        employee = mixer.blend(Employee)

        data_required = {
            "emp_no": 101,
            "emp_name": "Test Name",
            "emp_address": "Test Address",
            "emp_salary": 50000,
            "emp_position": "project_manager",
            "emp_present": False,
        }

        #Call URL
        url1 = reverse('emp-api-detail',kwargs={'pk':1})
        response = self.client.put(url1,data=data_required)

        # Check if resource Created or not
        assert response.json != None

        # Affirm status Code for Create Resource
        assert response.status_code == 200

        #Affirm employee names
        assert response.json()['emp_name'] == 'Test Name'
        assert response.json()['emp_address'] == 'Test Address'


    # Testing Partial Update API ViewSet
    def test_employee_api_partial_update(self):
        #Create Two Employees/Resources using mixer
        employee1 = mixer.blend(Employee,emp_name='John Doe',emp_address="Pune")
        employee2 = mixer.blend(Employee, emp_name='Jane Doe',emp_salary=50000)

        data_required_employee_1 = {
            "emp_name": "Test Name1",
            "emp_address": "New Delhi",
        }
        data_required_employee_2 = {
            "emp_name": "Test Name2",
            "emp_salary": 80000,
        }

        #Call URL
        url1 = reverse('emp-api-detail',kwargs={'pk':1})
        response1 = self.client.patch(url1,data=data_required_employee_1)
        url2 = reverse('emp-api-detail',kwargs={'pk':2})
        response2 = self.client.patch(url2,data=data_required_employee_2)

        # Check if resource Created or not
        assert response1.json != None
        assert response2.json != None

        # Affirm status Code for Create Resource
        assert response1.status_code == 200
        assert response2.status_code == 200

        #Affirm employee names
        assert response1.json()['emp_name'] == 'Test Name1'
        assert response2.json()['emp_name'] == 'Test Name2'


    # Testing Partial Update API ViewSet
    def test_employee_api_delete(self):
        #Create Two Employees/Resources using mixer
        employee1 = mixer.blend(Employee,emp_name='John Doe')
        employee2 = mixer.blend(Employee, emp_name='Jane Doe')

        #Affirm count of Employee Created
        assert Employee.objects.count() == 2

        #Call URL to delete resources
        url1 = reverse('emp-api-detail',kwargs={'pk':1})
        response1 = self.client.delete(url1)
        url2 = reverse('emp-api-detail',kwargs={'pk':2})
        response2 = self.client.delete(url2)

        # Affirm status Code for Create Resource
        assert response1.status_code == 204
        assert response2.status_code == 204

        #Affirm no of employees deleted
        assert Employee.objects.count() == 0










